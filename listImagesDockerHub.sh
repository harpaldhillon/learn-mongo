#!/bin/bash

# Function to fetch Docker tags and their modified dates for a given image
# Arguments:
#   $1: Docker image name (e.g., "nginx")
get_docker_tags_with_dates() {
    local image_name="$1"
    local page=1
    local total_pages=10

    # Initialize an array to store tag-date pairs
    local tags_with_dates=()

    while [ $page -le $total_pages ]; do
        local tags_url="https://hub.docker.com/v2/repositories/$image_name/tags/?page=$page&page_size=100"
        local tags_response=$(curl -sSL "$tags_url")

        if [ "$(echo "$tags_response" | jq -r '.next')" == "null" ]; then
	    break
        fi

        # Extract tags and their modified dates from the response
        local tags=$(echo "$tags_response" | jq -r '.results[] | "\(.name),\(.last_updated)"')

        # Append tag-date pairs to the array
        while IFS=',' read -r tag modified_date; do
            tags_with_dates+=("{\"name\": \"$tag\", \"modified_date\": \"$modified_date\"}")
        done <<< "$tags"

        # Increment page counter
        ((page++))
    done

    # Output the array as a JSON array
    #echo "[${tags_with_dates[*]}]"
    local json_array=$(IFS=,; echo "[${tags_with_dates[*]}]")
    echo "$json_array"
}

# Main script
if [ $# -eq 0 ]; then
    echo "Usage: $0 <image_name>"
    exit 1
fi

image_name="$1"
tags_json=$(get_docker_tags_with_dates "$image_name")

#echo "Now print array"
echo "$tags_json"

count_json_elements() {
    local json="$1"
    local count=$(echo "$json" | jq '. | length')
    echo "$count"
}

element_count=$(count_json_elements "$tags_json")
echo "Number of elements: $element_count"
