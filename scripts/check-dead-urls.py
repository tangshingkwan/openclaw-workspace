#!/usr/bin/env python3
import asyncio
import httpx
import json
from pathlib import Path

async def check_url(client, url, timeout=5):
    try:
        r = await client.get(url, timeout=timeout, follow_redirects=True)
        return url, r.status_code, None
    except Exception as e:
        return url, None, str(e)[:50]

async def main():
    with open('data/bookmarks_analysis.json') as f:
        data = json.load(f)
    
    # Check old HK/finance urls
    old_hk = [
        "http://www.aastocks.com/chi/ipo/default.asp",
        "http://news.bbc.co.uk/",
        "http://www.bloomberg.com/",
        "http://money18.on.cc/index.html",
        "http://www.hkcd.com.hk/",
        "http://mytv.tvb.com/news/inews/live",
        "http://www.hkej.com/template/landing11/jsp/main.jsp",
        "http://www.atnext.com/index.cfm",
        "http://forum9.hkgolden.com/view.aspx?type=BW&message=2993878",
        "http://www.gloryskygroup.com/index.aspx?lang=big5",
        "http://calc.waylonchan.net/",
        "http://currencywar.blog.hexun.com/",
        "http://www.aastocks.com/tc/default.aspx",
        "http://www.bbc.co.uk/worldservice/learningenglish/newsenglish/witn/index.shtml",
        "http://people2.com.tw/",
        "https://www.coursera.org/courses",
    ]
    
    async with httpx.AsyncClient() as client:
        tasks = [check_url(client, url) for url in old_hk]
        results = await asyncio.gather(*tasks)
    
    print("URL CHECK RESULTS:")
    print("=" * 60)
    for url, status, err in results:
        if status:
            if status == 200:
                print(f"✅ {status}  {url[:70]}")
            else:
                print(f"⚠️  {status}  {url[:70]}")
        else:
            print(f"❌ DEAD  {url[:70]}")
            if err:
                print(f"      ({err})")
    
    # Save results
    results_data = {"old_url_checks": [{"url": r[0], "status": r[1], "error": r[2]} for r in results]}
    with open('data/url_check_results.json', 'w') as f:
        json.dump(results_data, f, indent=2)

asyncio.run(main())
