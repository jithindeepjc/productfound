#!/bin/bash
set -e

echo "=== Productfound Market Analysis ==="
echo ""

ANALYSIS_TYPE="${1:-gaps}"

case "$ANALYSIS_TYPE" in
  gaps|market-gaps)
    echo "Analyzing market gaps — identifying underserved vs crowded categories..."
    echo ""
    productfound analyze gaps
    ;;
  competitive)
    CATEGORY="${2:-}"
    if [ -n "$CATEGORY" ]; then
      echo "Competitive analysis for: $CATEGORY"
      echo ""
      productfound analyze competitive --category "$CATEGORY"
    else
      echo "Competitive landscape across all categories..."
      echo ""
      productfound analyze competitive
    fi
    ;;
  persona)
    echo "Persona-based opportunity breakdown..."
    echo ""
    productfound analyze persona
    ;;
  trends)
    echo "Trend analysis — models by effort, tags by monetization speed..."
    echo ""
    productfound analyze trends
    ;;
  stats)
    echo "Dataset statistics..."
    echo ""
    productfound analyze stats
    ;;
  *)
    echo "Usage: analyze-market.sh [type]"
    echo ""
    echo "Types:"
    echo "  gaps          Market gap analysis (default)"
    echo "  competitive   Competitive landscape"
    echo "  persona       Persona-based breakdown"
    echo "  trends        Trend analysis"
    echo "  stats         Dataset statistics"
    exit 1
    ;;
esac
