#!/bin/bash
set -e

echo "=== Productfound Idea Search ==="
echo ""

MODEL=""
EFFORT=""
SPEED=""
CATEGORY=""
KEYWORD=""
PERSONA=""
TAGS=""
COUNT=20

while [[ $# -gt 0 ]]; do
  case "$1" in
    --model) MODEL="$2"; shift 2;;
    --effort) EFFORT="$2"; shift 2;;
    --speed) SPEED="$2"; shift 2;;
    --category) CATEGORY="$2"; shift 2;;
    --persona) PERSONA="$2"; shift 2;;
    --keyword|-k) KEYWORD="$2"; shift 2;;
    --tags) TAGS="$2"; shift 2;;
    --count|-n) COUNT="$2"; shift 2;;
    --all|-a) COUNT=9999; shift;;
    --detail|-d) DETAIL="--detail"; shift;;
    --help|-h)
      echo "Usage: search.sh [options]"
      echo ""
      echo "Options:"
      echo "  --model <m>       Business model (Freemium, Subscription, SaaS, etc.)"
      echo "  --effort <e>      Effort (Weekend Project, 1-3 Months, 3-6 Months, 6+ Months)"
      echo "  --speed <s>       Monetization speed (Quick Cash, Medium Runway, Long Game)"
      echo "  --category <c>    Industry category (DevTools, Health, Fintech, etc.)"
      echo "  --persona <p>     Builder persona"
      echo "  --keyword, -k <k> Search keyword"
      echo "  --tags <t>        Comma-separated tags"
      echo "  --count, -n <n>   Results to show (default 20)"
      echo "  --all, -a         Show all results"
      echo "  --detail, -d      Show full details"
      echo "  --help, -h        This help"
      exit 0;;
    *) echo "Unknown option: $1"; exit 1;;
  esac
done

CMD="productfound search"
[ -n "$MODEL" ] && CMD="$CMD --model \"$MODEL\""
[ -n "$EFFORT" ] && CMD="$CMD --effort \"$EFFORT\""
[ -n "$SPEED" ] && CMD="$CMD --speed \"$SPEED\""
[ -n "$CATEGORY" ] && CMD="$CMD --category \"$CATEGORY\""
[ -n "$KEYWORD" ] && CMD="$CMD --keyword \"$KEYWORD\""
[ -n "$PERSONA" ] && CMD="$CMD --persona \"$PERSONA\""
[ -n "$TAGS" ] && CMD="$CMD --tags \"$TAGS\""
[ -n "$DETAIL" ] && CMD="$CMD --detail"
CMD="$CMD --count $COUNT"

echo "Running: $CMD"
echo ""
eval $CMD 2>/dev/null || {
  echo "ERROR: productfound CLI not found. Install with: pip install productfound" >&2
  exit 1
}
