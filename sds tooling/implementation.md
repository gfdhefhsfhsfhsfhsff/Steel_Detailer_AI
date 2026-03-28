# 🧠 Implementation Details

## 🏛️ Technical Architecture
The scraper is a single **Node.js** application that automates a headless **Chromium** browser via **Playwright**.

### Key Flow
1. **TOC Extraction**: Uses `axios` to fetch the central `toc.html` for both API and Tutorials. `cheerio` parses the links from these tables of contents.
2. **Worker Pool**: Maintains a shared queue of links. Three parallel workers (`async function worker()`) "steal" items from the queue until it's empty.
3. **PDF Generation**: Every item's detail page is navigated to. Once `domcontentloaded` is triggered, the `page.pdf()` method is called to produce a high-fidelity snapshot.
4. **Markdown Transformation**: The `article.content` or main container is captured, then processed by `node-html-markdown` to convert HTML elements (tables, code snippets) into clean Markdown.
5. **Folder Hierarchies**: `itemName.split('.')` creates nested folder structures (e.g., `DesignData\SDS2\Database`) to match the .NET namespace structure.

## ⚙️ Configuration
The concurrency level is currently set to **3** to balance performance and network stability. This can be tuned in `scraper.js`:
```javascript
const CONCURRENCY = 3;
```

## 🛠️ Performance Optimizations
- **Resumability**: Uses `fs.existsSync(pdfPath) && fs.existsSync(mdPath)` to check if a documentation page has already been processed before making a network request.
- **Header Selection**: Captures specifically the `article.content` or `#main` content to avoid including repetitive headers/sidebars in the Markdown.

## 🚀 Execution Environment
- **Runtime**: Node.js 18+
- **Browser**: Playwright Chromium (Headless)
- **OS**: Works on Windows, macOS, and Linux.
