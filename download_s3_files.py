import boto3
from datetime import datetime, timezone
from pathlib import Path


def download_s3_files_by_date_range(
    bucket_name: str,
    start_day: int,
    end_day: int,
    year: int,
    month: int,
    local_dir: str = "./downloads",
    prefix: str = "",
):
    """
    Download S3 objects modified within a given day-of-month range.

    Args:
        bucket_name: S3 bucket name
        start_day: Start day of month (inclusive), e.g. 1
        end_day: End day of month (inclusive), e.g. 15
        year: Year (e.g. 2026)
        month: Month 1-12
        local_dir: Local directory to save files
        prefix: Optional S3 key prefix to filter (e.g. "logs/")
    """
    start_date = datetime(year, month, start_day, 0, 0, 0, tzinfo=timezone.utc)
    end_date = datetime(year, month, end_day, 23, 59, 59, tzinfo=timezone.utc)

    print(f"Filtering objects between {start_date} and {end_date}")

    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")

    local_path = Path(local_dir)
    local_path.mkdir(parents=True, exist_ok=True)

    downloaded = 0
    skipped = 0

    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            last_modified = obj["LastModified"]

            if start_date <= last_modified <= end_date:
                target = local_path / Path(key).name
                print(f"Downloading {key} -> {target}")
                s3.download_file(bucket_name, key, str(target))
                downloaded += 1
            else:
                skipped += 1

    print(f"\nDone. Downloaded: {downloaded}, Skipped: {skipped}")


if __name__ == "__main__":
    download_s3_files_by_date_range(
        bucket_name="my-bucket",
        start_day=1,
        end_day=15,
        year=2026,
        month=4,
        local_dir="./downloads",
        prefix="logs/",
    )
