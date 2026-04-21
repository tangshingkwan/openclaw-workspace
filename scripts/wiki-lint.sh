#!/bin/bash
# Fast wiki lint script - checks for common issues without AI

WIKI="/root/.openclaw/workspace/wiki"
ISSUES=0

echo "🔍 Wiki Lint Report - $(date '+%Y-%m-%d')"
echo "========================================"
echo ""

# Check for orphan raw files (exist but not sourced)
echo "📄 Orphaned Raw Files (no wiki page):"
ORPHANS=$(find "$WIKI/raw" -name "*.md" 2>/dev/null | while read f; do
  NAME=$(basename "$f" .md)
  if [ ! -f "$WIKI/sources/${NAME,,}.md" ] && [ ! -f "$WIKI/sources/${NAME}.md" ]; then
    echo "  - $NAME"
    ISSUES=$((ISSUES+1))
  fi
done)
if [ -z "$ORPHANS" ]; then
  echo "  ✅ None found"
else
  echo "$ORPHANS"
fi
echo ""

# Check for broken [[cross-references]]
echo "🔗 Checking [[cross-references]]..."
BROKEN=0
for f in "$WIKI/sources"/*.md; do
  if [ -f "$f" ]; then
    LINKS=$(grep -o '\[\[[^]]*\]\]' "$f" 2>/dev/null | tr -d '[]' | tr '[:upper:]' '[:lower:]')
    for LINK in $LINKS; do
      if [ ! -f "$WIKI/sources/$LINK.md" ] && [ ! -f "$WIKI/sources/$(echo $LINK | tr '[:lower:]' '[:upper:]').md" ]; then
        if [ "$LINK" != "synagie-api" ]; then  # skip known placeholder
          echo "  ⚠️  $(basename $f): [[$LINK]] → not found"
          BROKEN=$((BROKEN+1))
        fi
      fi
    done
  fi
done
if [ $BROKEN -eq 0 ]; then
  echo "  ✅ All links valid"
else
  echo "  ⚠️  $BROKEN broken links"
  ISSUES=$((ISSUES+BROKEN))
fi
echo ""

# Check for stale INDEX date
echo "📅 INDEX.md date check:"
INDEX_DATE=$(grep -i "last updated" "$WIKI/INDEX.md" 2>/dev/null | head -1)
echo "  $INDEX_DATE"
echo ""

# Count sources
SOURCE_COUNT=$(ls "$WIKI/sources"/*.md 2>/dev/null | wc -l)
echo "📊 Stats:"
echo "  Sources: $SOURCE_COUNT"
echo "  Raw files: $(find $WIKI/raw -name '*.md' 2>/dev/null | wc -l)"
echo ""

if [ $ISSUES -gt 0 ]; then
  echo "⚠️  Found $ISSUES issues - review above"
else
  echo "✅ No issues found"
fi
