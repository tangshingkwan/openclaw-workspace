#!/usr/bin/env node
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const CREATORS = {
  'kelileo': 'https://www.patreon.com/cw/KelileoCUP',
  'calvin_choy': 'https://www.patreon.com/c/CalvinChoy',
  'et_trading': 'https://www.patreon.com/cw/u66833541'
};

const cookies = JSON.parse(fs.readFileSync(path.join(__dirname, '../patreon-cookies.json'), 'utf8'));

async function fetchPosts() {
  const results = {};
  const timestamp = new Date().toISOString();
  
  for (const [key, url] of Object.entries(CREATORS)) {
    console.log(`Fetching ${key}...`);
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext();
    await context.addCookies(cookies);
    const page = await context.newPage();
    
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
      await page.waitForTimeout(5000);
      
      const content = await page.evaluate(() => {
        window.scrollTo(0, document.body.scrollHeight);
        return document.body.innerText;
      });
      
      results[key] = {
        url,
        fetchedAt: timestamp,
        content: content.slice(0, 15000)
      };
      
    } catch (e) {
      console.log(`Error fetching ${key}: ${e.message}`);
      results[key] = { error: e.message, fetchedAt: timestamp };
    }
    
    await browser.close();
    await new Promise(r => setTimeout(r, 2000));
  }
  
  const outputPath = path.join(__dirname, '../patreon-posts.json');
  fs.writeFileSync(outputPath, JSON.stringify(results, null, 2));
  console.log(`Saved to ${outputPath}`);
  
  // Also save with timestamp for history
  const dateStr = new Date().toISOString().split('T')[0];
  const historyPath = path.join(__dirname, `../patreon-history/${dateStr}.json`);
  const historyDir = path.dirname(historyPath);
  if (!fs.existsSync(historyDir)) fs.mkdirSync(historyDir, { recursive: true });
  fs.writeFileSync(historyPath, JSON.stringify(results, null, 2));
  console.log(`History saved to ${historyPath}`);
}

fetchPosts().catch(console.error);
