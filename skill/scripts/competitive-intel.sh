#!/bin/bash
set -e

echo "=== Loot Drop Competitive Intelligence ==="
echo ""

CATEGORY="${1:-}"
KEYWORD="${2:-}"

if [ -z "$CATEGORY" ]; then
  echo "Usage: competitive-intel.sh <category> [keyword-filter]"
  echo ""
  echo "Examples:"
  echo "  competitive-intel.sh DevTools"
  echo "  competitive-intel.sh Health AI"
  echo "  competitive-intel.sh Fintech"
  echo ""
  echo "Available categories:"
  loot categories 2>/dev/null || echo "  (install loot CLI: pip install loot-cli)"
  exit 1
fi

echo "Competitive intelligence for: $CATEGORY"
echo ""

# Full competitive analysis for this category
loot analyze competitive --category "$CATEGORY" 2>/dev/null || {
  echo "ERROR: loot CLI not found. Install with: pip install loot-cli" >&2
  exit 1
}

echo "---"
echo "Ideas in this category:"
echo ""

SEARCH_CMD="loot search --category \"$CATEGORY\" --all"
[ -n "$KEYWORD" ] && SEARCH_CMD="$SEARCH_CMD --keyword \"$KEYWORD\""
eval $SEARCH_CMD

echo ""
echo "--- Tags in this category ---"
loot tags --category "$CATEGORY" --counts 2>/dev/null

echo ""
echo "--- Recommended models for $CATEGORY ---"
loot search --category "$CATEGORY" --all --detail 2>/dev/null | grep -i "Model:" | sort | uniq -c | sort -rn
