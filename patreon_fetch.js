const { chromium } = require('playwright');

const cookies = [
  {name: 'session_id', value: '7HLh_oOcTd2l_GkfiP1F2IEJrEG2U8umDFnbaf181QM', domain: 'www.patreon.com', path: '/', secure: true},
  {name: 'group_id', value: '44b0ce3e38d86a5191132e6947d9d68810d4cd26553bb04098730481f0a015a6', domain: '.patreon.com', path: '/'},
  {name: 'patreon_device_id', value: '2e0ffc86-050f-4260-871d-eb32abbed28d', domain: 'www.patreon.com', path: '/'},
  {name: 'patreon_locale_code', value: 'en-US', domain: 'www.patreon.com', path: '/'},
  {name: 'patreon_location_country_code', value: 'HK', domain: 'www.patreon.com', path: '/'},
];

async function fetchCreator(creatorName, url) {
  console.log(`\n=== ${creatorName} ===`);
  
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  await context.addCookies(cookies);
  const page = await context.newPage();
  
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(5000);
    
    // Get page text content
    const content = await page.evaluate(() => {
      // Scroll down to load more content
      window.scrollTo(0, document.body.scrollHeight);
      return document.body.innerText;
    });
    
    // Parse posts - look for patterns like "X days ago" or dates
    const lines = content.split('\n').filter(l => l.trim());
    const posts = [];
    let currentPost = null;
    
    for (const line of lines) {
      // Look for post titles (usually followed by content)
      if (line.match(/\d+\s*(hours?|days?|minutes?|ago)/i) || line.match(/\d{4}.*\d{2}.*\d{2}/)) {
        if (currentPost) posts.push(currentPost);
        currentPost = { date: line, content: '' };
      } else if (currentPost && line.length > 50) {
        currentPost.content += line + ' ';
      }
    }
    if (currentPost) posts.push(currentPost);
    
    console.log(`Found ${posts.length} posts`);
    posts.slice(0, 3).forEach((p, i) => {
      console.log(`\n--- Post ${i+1} [${p.date}] ---`);
      console.log(p.content.slice(0, 200) + '...');
    });
    
  } catch (e) {
    console.log(`Error: ${e.message}`);
  }
  
  await browser.close();
}

// Fetch 茄利略・CUP first as a test
fetchCreator('茄利略・CUP', 'https://www.patreon.com/cw/KelileoCUP');
