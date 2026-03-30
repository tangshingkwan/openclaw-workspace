#!/usr/bin/env python3
"""Parse Chrome bookmarks HTML properly (recursive)."""
import re
from datetime import datetime, timezone
from collections import Counter
import json

def parse_bookmarks_html(content):
    """Parse Chrome bookmarks HTML recursively."""
    bookmarks = []
    folders = []
    
    # Find the main bookmark bar content
    # Chrome exports as nested <DL><p>...content...</DL>
    
    def extract_folder(html):
        """Extract bookmarks from a <DL>...</DL> block."""
        items = []
        # Find all top-level DT entries
        dt_pattern = re.compile(r'<DT>(.*?)(?=<DT>|<H3|$)', re.DOTALL | re.IGNORECASE)
        
        for match in dt_pattern.finditer(html):
            block = match.group(1).strip()
            
            # Check if it's a folder (H3)
            h3_match = re.search(r'<H3[^>]*>(.*?)</H3>', block, re.IGNORECASE)
            if h3_match:
                folder_name = h3_match.group(1).strip()
                folders.append(folder_name)
                # Find the nested DL content
                dl_match = re.search(r'<DL[^>]*>(.*?)</DL>', block, re.DOTALL | re.IGNORECASE)
                if dl_match:
                    nested_html = dl_match.group(1)
                    nested_bookmarks = extract_bookmarks_from_dl(nested_html)
                    for b in nested_bookmarks:
                        b['folder'] = folder_name
                    items.extend(nested_bookmarks)
            else:
                # Check if it's a bookmark (A tag)
                a_match = re.search(r'<A[^H]*HREF="([^"]*)"[^>]*>(.*?)</A>', block, re.DOTALL | re.IGNORECASE)
                if a_match:
                    url = a_match.group(1).strip()
                    title = re.sub(r'<[^>]+>', '', a_match.group(2)).strip()
                    title = re.sub(r'\s+', ' ', title)
                    
                    add_date_match = re.search(r'ADD_DATE="(\d+)"', block)
                    add_date = int(add_date_match.group(1)) if add_date_match else 0
                    
                    icon_match = re.search(r'ICON="([^"]+)"', block)
                    has_icon = bool(icon_match)
                    
                    if url:
                        items.append({
                            'title': title,
                            'url': url,
                            'add_date': add_date,
                            'has_icon': has_icon,
                            'folder': '',
                        })
        return items
    
    def extract_bookmarks_from_dl(html):
        """Extract bookmarks from a <DL> block."""
        items = []
        # Remove top-level DL wrapper to process children
        html = re.sub(r'^<DL[^>]*>', '', html, count=1)
        html = re.sub(r'</DL>\s*$', '', html)
        
        pos = 0
        while pos < len(html):
            # Find next DT block
            dt_match = re.search(r'<DT>(.*?)(?=<DT>|$)', html[pos:], re.DOTALL | re.IGNORECASE)
            if not dt_match:
                break
            pos += dt_match.end()
            block = dt_match.group(1)
            
            # Check if it's a folder (contains H3)
            h3_m = re.search(r'<H3[^>]*>(.*?)</H3>', block, re.IGNORECASE)
            if h3_m:
                folder_name = h3_m.group(1).strip()
                folders.append(folder_name)
                # Find nested DL content
                dl_m = re.search(r'<DL[^>]*>(.*?)</DL>', block, re.DOTALL | re.IGNORECASE)
                if dl_m:
                    nested = extract_bookmarks_from_dl(dl_m.group(1))
                    for b in nested:
                        b['folder'] = folder_name
                    items.extend(nested)
            else:
                # It's a bookmark
                a_m = re.search(r'<A[^>]*HREF="([^"]*)"[^>]*>(.*?)</A>', block, re.DOTALL | re.IGNORECASE)
                if a_m:
                    url = a_m.group(1).strip()
                    title = re.sub(r'<[^>]+>', '', a_m.group(2)).strip()
                    title = re.sub(r'\s+', ' ', title)
                    add_d = re.search(r'ADD_DATE="(\d+)"', block)
                    icon_m = re.search(r'ICON="([^"]+)"', block)
                    add_date = int(add_d.group(1)) if add_d else 0
                    if url:
                        items.append({
                            'title': title,
                            'url': url,
                            'add_date': add_date,
                            'has_icon': bool(icon_m),
                            'folder': '',
                        })
        return items
    
    # Find all top-level DL blocks
    dl_pattern = re.compile(r'<DL[^>]*>(.*?)</DL>', re.DOTALL | re.IGNORECASE)
    for dl_match in dl_pattern.finditer(content):
        dl_content = dl_match.group(1)
        items = extract_bookmarks_from_dl(dl_content)
        bookmarks.extend(items)
    
    return bookmarks, folders

with open("/root/.openclaw/workspace/data/bookmarks_raw.html", "r", encoding="utf-8") as f:
    content = f.read()

bookmarks, folders = parse_bookmarks_html(content)

# Deduplicate
seen_urls = set()
unique = []
dupes = []
for b in bookmarks:
    if b['url'] and b['url'] not in seen_urls:
        seen_urls.add(b['url'])
        unique.append(b)
    elif b['url']:
        dupes.append(b)

now_ts = datetime.now(timezone.utc).timestamp()
one_yr_ago = now_ts - 365 * 86400
three_yr_ago = now_ts - 3 * 365 * 86400

old = [b for b in unique if 0 < b['add_date'] < one_yr_ago]
very_old = [b for b in unique if 0 < b['add_date'] < three_yr_ago]

# Domain analysis
domain_count = Counter()
for b in unique:
    try:
        from urllib.parse import urlparse
        p = urlparse(b['url'])
        dom = p.netloc.replace('www.', '').replace('m.', '')
        if dom:
            domain_count[dom] += 1
    except:
        pass

print("=" * 60)
print("📚 BOOKMARKS ANALYSIS")
print("=" * 60)
print(f"Total raw:          {len(bookmarks)}")
print(f"Unique bookmarks:   {len(unique)}")
print(f"Duplicates:         {len(dupes)}")
print(f"Older than 1 year:  {len(old)}")
print(f"Older than 3 years: {len(very_old)}")
print(f"")
print(f"📁 Folders ({len(folders)}):")
for f in folders:
    count = len([b for b in unique if b.get('folder') == f])
    print(f"   [{count:3d}] {f}")
print(f"")
print(f"🔗 Top Domains:")
for dom, cnt in domain_count.most_common(15):
    print(f"   {cnt:3d}  {dom}")
print(f"")
print(f"⚠️  Very Old Bookmarks (>3 years):")
for b in sorted(very_old, key=lambda x: x['add_date'])[:20]:
    ts = datetime.fromtimestamp(b['add_date'], tz=timezone.utc).strftime('%Y-%m-%d') if b['add_date'] > 0 else 'unknown'
    print(f"   [{ts}] {b['title'][:50]}")
    print(f"             {b['url'][:70]}")
    print(f"             folder: {b.get('folder','')}")
    print()

# Save full analysis
analysis = {
    'summary': {
        'total_raw': len(bookmarks),
        'total_unique': len(unique),
        'duplicates': len(dupes),
        'older_than_1yr': len(old),
        'older_than_3yr': len(very_old),
    },
    'folders': folders,
    'domains': dict(domain_count.most_common(20)),
    'very_old_bookmarks': sorted(very_old, key=lambda x: x['add_date']),
    'duplicate_bookmarks': dupes,
    'all_bookmarks': unique,
}
with open('/root/.openclaw/workspace/data/bookmarks_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(analysis, f, indent=2, ensure_ascii=False)
print(f"✅ Full analysis saved to data/bookmarks_analysis.json")
print(f"   ({len(unique)} bookmarks stored)")
