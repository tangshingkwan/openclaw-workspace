#!/usr/bin/env node
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const CREATORS = {
  'kelileo': 'https://www.patreon.com/cw/KelileoCUP',
  'calvin_choy': 'https://www.patreon.com/c/CalvinChoy'
};

const cookies = JSON.parse(fs.readFileSync(path.join(__dirname, '../patreon-cookies.json'), 'utf8'));

async function fetchAllPosts() {
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
      
      // Scroll multiple times to load more posts
      for (let i = 0; i < 5; i++) {
        await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
        await page.waitForTimeout(2000);
      }
      
      const content = await page.evaluate(() => {
        return document.body.innerText;
      });
      
      results[key] = {
        url,
        fetchedAt: timestamp,
        content: content.slice(0, 50000)
      };
      
    } catch (e) {
      console.log(`Error fetching ${key}: ${e.message}`);
      results[key] = { error: e.message, fetchedAt: timestamp };
    }
    
    await browser.close();
    await new Promise(r => setTimeout(r, 3000));
  }
  
  const outputPath = path.join(__dirname, '../patreon-posts-week.json');
  fs.writeFileSync(outputPath, JSON.stringify(results, null, 2));
  console.log(`Saved to ${outputPath}`);
  return results;
}

fetchAllPosts().catch(console.error);
