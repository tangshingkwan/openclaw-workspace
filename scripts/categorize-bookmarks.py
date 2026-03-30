#!/usr/bin/env python3
import json
from urllib.parse import urlparse

with open('/root/.openclaw/workspace/data/bookmarks_analysis.json') as f:
    data = json.load(f)

all_bm = data['all_bookmarks']

dead_urls = {"http://mytv.tvb.com/news/inews/live", "http://www.atnext.com/index.cfm",
             "http://www.gloryskygroup.com/index.aspx?lang=big5",
             "http://currencywar.blog.hexun.com/", "http://people2.com.tw/"}

seen = set()
good = []
for b in all_bm:
    if b['url'] not in dead_urls and b['url'] not in seen:
        seen.add(b['url'])
        good.append(b)

cats = {
    "Tech & Coding": [],
    "AI & Productivity": [],
    "Amazon Selling & FBA": [],
    "Trading & Finance": [],
    "English Learning": [],
    "Travel & Backpacking": [],
    "Jobs & Recruitment": [],
    "Work Tools": [],
    "Design & Creativity": [],
    "Shopping & Logistics": [],
    "HK Life": [],
    "Media & Entertainment": [],
    "Lifestyle": [],
}

# Precompute sets for fast lookup
tech_doms = {'npmjs.com','github.com','stackoverflow.com','pypi.org','developer.mozilla.org',
    'w3schools.com','codecademy.com','edx.org','khanacademy.org','freecodecamp.org',
    'theodinproject.com','leetcode.com','hackerrank.com','codewars.com','topcoder.com',
    'codeforces.com','codingame.com','coderbyte.com','edabit.com','projecteuler.net',
    'codesandbox.io','codepen.io','replit.com','dev.to','devdocs.io','git-scm.com',
    'yarnpkg.com','expressjs.com','flask.palletsprojects.com','fastapi.tiangolo.com',
    'reactjs.org','vuejs.org','angular.io','svelte.dev','jquery.com','webpack.js.org',
    'parceljs.org','vitejs.dev','deno.land','bun.sh','rust-lang.org','go.dev',
    'python.org','nodejs.org','typescriptlang.org','reactnative.dev','flutter.dev',
    'dart.dev','django.com','laravel.com','rails.com','spring.io','jupyter.org',
    'colab.research.google.com','kaggle.com','huggingface.co','arxiv.org',
    'codesignal.com','exercism.io','datacamp.com','dataquest.io','plotly.com',
    'shinyapps.io','gradio.app','d3js.org','threejs.org','chartjs.org',
    'greensock.com','gsap.com','popmotion.io','scrollmagic.io','tailwindcss.com',
    'getbootstrap.com','bulma.io','chakra-ui.com','radix-ui.com','makeuseof.com',
    'engadget.com','cnet.com','theverge.com','wired.com','techcrunch.com',
    'arstechnica.com','mashable.com','digitaltrends.com','pcmag.com','laptopmag.com',
    'androidcentral.com','9to5mac.com','macrumors.com','appleinsider.com','ifanr.com'}

ai_doms = {'openai.com','anthropic.com','claude.ai','gemini.google','copilot.github.com',
    'cursor.sh','windsurf.com','codeium.com','tabnine.com','poe.com','perplexity.ai',
    'you.com','phind.com','deepseek.com','mistral.ai','cohere.ai','ai21.com',
    'stability.ai','midjourney.com','runwayml.com','leonardo.ai','civitai.com',
    'Paperswithcode.com','replicate.com','runpod.io','langchain.com','llamaindex.ai',
    'chainlit.io','gradio.app','streamlit.io','tensorboard.dev','mlflow.org',
    'wandb.ai','notion.so','evernote.com','bear.app','notable.app','airtable.com',
    'basecamp.com','wrike.com','smartsheet.com','asana.com','monday.com',
    'clickup.com','trello.com','todoist.com','ticktick.com','habitica.com',
    'headspace.com','calm.com','grammarly.com','quillbot.com','prowritingaid.com'}

amazon_doms = {'junglescout.com','keepa.com','camelcamelcamel.com','merchantwords.com',
    'amztracker.com','helium10.com','sellics.com','sellbrite.com','bqool.com',
    'channeladvisor.com','feedvisor.com'}

trading_doms = {'tradingview.com','investopedia.com','babypips.com','forexfactory.com',
    'mql5.com','investing.com','stockcharts.com','finviz.com','bloomberg.com',
    'reuters.com','cnbc.com','marketwatch.com','economist.com','ft.com','wsj.com',
    'seekingalpha.com','macrotrends.net','dailyfx.com','fxstreet.com','myfxbook.com',
    'etoro.com','plus500.com','oanda.com','fxcm.com','dukascopy.com','swissquote.com',
    'aastocks.com','etnet.com.hk','money18.on.cc','hkex.com.hk','hkej.com','hkcd.com.hk',
    'babypips.com','forexfactory.com'}

eng_doms = {'bbc.co.uk','bbc.com','voicetube.com','voicetube.tw','englishclub.com',
    'cambly.com','talkenglish.com','englishpage.com','duolingo.com','lingoda.com',
    'babbel.com','rosettastone.com','busuu.com','memrise.com','ankiweb.net',
    'forvo.com','youglish.com','lingq.com','pimsleur.com',
    'oxfordlearnersdictionaries.com','dictionary.cambridge.org','merriam-webster.com',
    'collinsdictionary.com','wordreference.com','yourdictionary.com',
    'thefreedictionary.com','urbandictionary.com','engvid.com','englishcentral.com'}

travel_doms = {'hostelworld.com','booking.com','airbnb.com','agoda.com','couchsurfing.com',
    'workaway.info','helpx.net','wwoof.net','wwoof.com','trains.se','eurail.com',
    'rome2rio.com','busabout.com','nationalexpress.com','megabus.com','flixbus.com',
    'blablacar.com','skyscanner.com','kayak.com','momondo.com','expedia.com',
    'hotels.com','trivago.com','lonelyplanet.com','roughguides.com','nomadicmatt.com',
    'tripadvisor.com'}

jobs_doms = {'jobsdb.com','ctgoodjobs.hk','indeed.com','indeed.co.uk','monster.com',
    'careerjet.com','careerjet.co.uk','linkedin.com','glassdoor.com',
    'jobmarket.com.hk','recruit.com.hk','jobstreet.com','seek.com.au','neuvoo.com',
    'careerbuilder.com','simplyhired.com','ziprecruiter.com','fiverr.com',
    'freelancer.com','upwork.com','toptal.com','gun.io','turing.com',
    'peopleperhour.com','99designs.com','cv-library.co.uk','cwjobs.co.uk',
    'fish4.co.uk','jobsite.co.uk','reed.co.uk','totaljobs.com'}

work_doms = {'sharepoint.com','tiffanyo365.sharepoint.com','louisvuittonmalletier.sharepoint.com',
    'shiseidogroup.atlassian.net','shiseidomalaysia-my.sharepoint.com',
    'rciapac.sharepoint.com','vsod-my.sharepoint.com','atlassian.net','lassian.com',
    'confluence.atlassian','jira.atlassian','bitbucket.org','asana.com','monday.com',
    'clickup.com','notion.so','slack.com','teams.microsoft','hubspot.com',
    'salesforce.com','trailhead.salesforce','zendesk.com','freshdesk.com',
    'intercom.com','outlook.office.com','office.com','cegid.cloud','cegid.com',
    'workday.com','servicenow.com','tableau.com','powerbi.microsoft','looker.com',
    'asana','notion','trello','monday','clickup','jira','confluence','slack',
    'teams','zoom.us','dropbox.com','box.com','airtable','basecamp','wrike','smartsheet'}

design_doms = {'dribbble.com','behance.net','pinterest.com','pinterest.co.uk',
    'graphicriver.net','themeforest.net','creativemarket.com','freepik.com',
    'unsplash.com','pexels.com','stocksnap.io','burst.shopify','kaboompics.com',
    'photock.com','foodiesfeed.com','librestock.com','iconfinder.com',
    'thenounproject.com','flaticon.com','fontawesome.com','ionic.io','heroicons.com',
    'lucide.dev','feathericons.com','fontello.com','fontsquirrel.com','fonts.com',
    'fonts.google.com','myfonts.com','colourlovers.com','coolors.co','paletton.com',
    'color.adobe.com','0to255.com','webgradients.com','cssgradient.com',
    'uigradients.com','awwwards.com','thefwa.com','cssdesignawards.com',
    'codrops.com','tympanus.net'}

shopping_doms = {'shopee.comy','lazada.coph','lazada.comy','lazada.com.ph',
    'shopee.com.my','taobao.com','alibaba.com','aliexpress.com','1688.com',
    'ebay.com','ebay.co.uk','amazon.com','walmart.com','target.com','bestbuy.com',
    'etsy.com','wish.com','gearbest.com','banggood.com','lightinthebox.com',
    'dhgate.com','shipbao.com','buyandship.today','buyippee.com','pieceup.hk',
    'lotpost.com','cubiclogistics.co.uk','us-ex.com','dou4la.com','4px.com',
    'sfcservice.com','dhl.com','fedex.com','ups.com','usps.com','ems.com.cn',
    'chinapost.com','hongkongpost.com','speedpost.com.hk','kerryexpress.com.hk',
    'sf-express.com','zto.com','yto.com','6pm.com','footlocker.com',
    'jimmyjazz.com','champssports.com','eastbay.com','finishline.com','zappos.com'}

hk_life_doms = {'unwire.hk','topick.hket.com','mingpao.com','singtao.com',
    'rthk.hk','scmp.com','hk01.com','vjmedia.com.hk','cnyes.com','28hse.com',
    'centaline.com','ricacorp.com','midland.com.hk','gohome.com.hk',
    'squarefoot.com.hk','propnoah.com','house730.com','property.hk','livno.com',
    'ctgoodjobs.hk','jobsdb.com','gov.hk','ird.gov.hk','sfc.hk','hkex.com.hk',
    'legco.gov.hk','e123.hk','wellsoon.hk','hkatv.com','uwants.com',
    'discuss.com.hk','moneyhouse.lauknow.com','gohome.cohk','midland.cohk',
    'kaifung.com','ecfinancialcareers.hk','efinancialcareers.hk'}

media_doms = {'youtube.com','vimeo.com','twitch.tv','netflix.com','disneyplus.com',
    'hbo.com','primevideo.com','apple.com/tv','spotify.com','soundcloud.com',
    'bandcamp.com','podbean.com','anchor.fm','overcast.fm','twitter.com','x.com',
    'instagram.com','facebook.com','tiktok.com','snapchat.com','reddit.com',
    'quora.com','medium.com','substack.com','medium.muzu','ghost.org',
    'substack.com','matters.news','lihkg.com','discuss.com.hk'}

def categorize(b):
    url = b['url'].lower()
    try:
        dom = urlparse(b['url']).netloc.replace('www.', '').replace('m.', '')
    except:
        dom = ''
    
    if dom in tech_doms:
        return "Tech & Coding"
    if dom in ai_doms or 'notion.so' in url or 'chat.openai' in url or 'chatgpt' in url or 'cursor.sh' in url or 'windsurf' in url or 'perplexity' in url:
        return "AI & Productivity"
    if dom in amazon_doms or any(x in url for x in ['sellercentral','junglescout','keepa.com','camelcamelcamel','merchantwords','amztracker','fba','amazon seller','amazon fba']):
        return "Amazon Selling & FBA"
    if dom in trading_doms or any(x in url for x in ['tradingview','investopedia','babypips','forexfactory','mql5','metatrader','ninjatrader','tradestation','interactivebrokers','etoro','aastocks','etnet','money18','hkex','babypips']):
        return "Trading & Finance"
    if dom in eng_doms:
        return "English Learning"
    if dom in travel_doms:
        return "Travel & Backpacking"
    if dom in jobs_doms or any(x in url for x in ['freelancer.com','upwork.com','fiverr.com']):
        return "Jobs & Recruitment"
    if dom in work_doms or any(x in url for x in ['sharepoint.com','atlassian.net','cegid.cloud','workday','salesforce','hubspot','zendesk']):
        return "Work Tools"
    if dom in design_doms:
        return "Design & Creativity"
    if dom in shopping_doms or any(x in url for x in ['shopee','lazada','taobao','alibaba','1688','ebay','shipbao','buyandship']):
        return "Shopping & Logistics"
    if dom in hk_life_doms or any(x in url for x in ['gov.hk','ird.gov.hk','sfc.hk','hkex.com.hk']):
        return "HK Life"
    if dom in media_doms or any(x in url for x in ['youtube.com','spotify.com','netflix.com','twitter.com','instagram.com','reddit.com','medium.com']):
        return "Media & Entertainment"
    return "Lifestyle"

for b in good:
    cat = categorize(b)
    cats[cat].append(b)

# Print counts
total = 0
for name, bm_list in sorted(cats.items(), key=lambda x: -len(x[1])):
    total += len(bm_list)
    print(f"  {len(bm_list):3d}  {name}")
print(f"  ---")
print(f"  {total:3d}  TOTAL")

with open('/tmp/bm_cats.json', 'w') as f:
    json.dump(cats, f)
print("\nSaved to /tmp/bm_cats.json")
