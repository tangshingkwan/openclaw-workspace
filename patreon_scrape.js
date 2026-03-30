const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();
  
  // Set cookies from the exported data
  const cookies = [
    {name: 'session_id', value: '7HLh_oOcTd2l_GkfiP1F2IEJrEG2U8umDFnbaf181QM', domain: 'www.patreon.com', path: '/'},
    {name: 'group_id', value: '44b0ce3e38d86a5191132e6947d9d68810d4cd26553bb04098730481f0a015a6', domain: '.patreon.com', path: '/'},
    {name: 'patreon_device_id', value: '2e0ffc86-050f-4260-871d-eb32abbed28d', domain: 'www.patreon.com', path: '/'},
    {name: 'patreon_locale_code', value: 'en-US', domain: 'www.patreon.com', path: '/'},
    {name: 'patreon_location_country_code', value: 'HK', domain: 'www.patreon.com', path: '/'},
    {name: '_ga', value: 'GA1.1.131885225.1774716661', domain: '.patreon.com', path: '/'},
  ];
  
  await context.addCookies(cookies);
  
  console.log('Navigating to Patreon...');
  await page.goto('https://www.patreon.com/cw/KelileoCUP', { waitUntil: 'domcontentloaded', timeout: 30000 });
  
  // Wait for content to render
  await page.waitForTimeout(5000);
  
  // Get page title
  const title = await page.title();
  console.log('Title:', title);
  
  // Try to get post content
  const bodyText = await page.evaluate(() => {
    return document.body.innerText.slice(0, 2000);
  });
  console.log('Body text:', bodyText);
  
  await browser.close();
})().catch(console.error);
