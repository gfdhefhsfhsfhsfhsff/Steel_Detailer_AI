const { chromium } = require('playwright');
const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');
const { NodeHtmlMarkdown } = require('node-html-markdown');

const VERSIONS = ['2025-1', '2026'];
const SECTIONS = [
    { id: 'API', path: 'net/api/', toc: 'net/api/toc.html' },
    { id: 'Tutorials', path: 'tutorial/', toc: 'tutorial/toc.html' }
];

const BASE_DOMAIN = 'https://developer.sds2.com/';
const OUTPUT_DIR = path.join(__dirname, 'output');

async function ensureDir(dir) {
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
}

async function scrapeSection(version, section, browser) {
    const sectionBaseUrl = `${BASE_DOMAIN}${version}/${section.path}`;
    const tocUrl = `${BASE_DOMAIN}${version}/${section.toc}`;
    
    console.log(`--- [${version}] Scraping Section: ${section.id} ---`);
    console.log(`Fetching TOC from ${tocUrl}...`);
    
    let response;
    try {
        response = await axios.get(tocUrl);
    } catch (err) {
        console.error(`Failed to fetch TOC for ${version}/${section.id}:`, err.message);
        return;
    }
    
    const $ = cheerio.load(response.data);
    const links = [];

    $('a').each((i, el) => {
        const href = $(el).attr('href');
        if (href && href.endsWith('.html') && !href.startsWith('http')) {
            links.push(href);
        }
    });

    console.log(`Found ${links.length} items in ${version}/${section.id}.`);

    const CONCURRENCY = 3;
    const queue = [...links.map((link, index) => ({ link, index }))];
    
    async function processItem(link, i) {
        const url = sectionBaseUrl + link;
        const itemName = link.replace('.html', '');
        const parts = itemName.split('.');
        
        // Structured path: output/version/section/parts
        const relativePath = path.join(version, section.id, ...parts);
        const itemDir = path.join(OUTPUT_DIR, relativePath);
        
        try {
            await ensureDir(itemDir);
            const pdfPath = path.join(itemDir, `${parts[parts.length-1]}.pdf`);
            const mdPath = path.join(itemDir, `${parts[parts.length-1]}.md`);

            if (fs.existsSync(pdfPath) && fs.existsSync(mdPath)) {
                return;
            }

            console.log(`[${version}] [${section.id}] [${i+1}/${links.length}] Scraping ${itemName}...`);
            const page = await browser.newPage();
            try {
                await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
                await page.waitForTimeout(1000);

                await page.pdf({
                    path: pdfPath,
                    format: 'A4',
                    printBackground: true,
                    margin: { top: '20px', right: '20px', bottom: '20px', left: '20px' }
                });

                const contentHtml = await page.innerHTML('article.content') || await page.innerHTML('#main') || await page.innerHTML('body');
                const markdown = NodeHtmlMarkdown.translate(contentHtml);
                fs.writeFileSync(mdPath, markdown);
            } finally {
                await page.close();
            }
        } catch (err) {
            console.error(`[${version}/${section.id}] Error scraping ${itemName}:`, err.message);
        }
    }

    async function worker() {
        while (queue.length > 0) {
            const item = queue.shift();
            if (!item) break;
            await processItem(item.link, item.index);
        }
    }

    await Promise.all(Array.from({ length: CONCURRENCY }).map(worker));
}

async function main() {
    const browser = await chromium.launch({ headless: true });
    for (const version of VERSIONS) {
        for (const section of SECTIONS) {
            await scrapeSection(version, section, browser);
        }
    }
    await browser.close();
    console.log('All configured versions and sections complete.');
}

main().catch(err => {
    console.error('Fatal Scraper Error:', err);
});
