repo="mcr.microsoft.com/tunnel/gateway/agent"; latest_digest=$(skopeo inspect docker://$repo:latest | jq -r .Digest); skopeo list-tags docker://$repo | jq -r '.Tags[]' | while read tag; do [ "$(skopeo inspect docker://$repo:$tag | jq -r .Digest)" = "$latest_digest" ] && echo "latest → $tag"; done
latest → 20250815.1
latest → 20250815.1-edge
latest → latest
latest → latest-fast
latest → latest-intermediate
