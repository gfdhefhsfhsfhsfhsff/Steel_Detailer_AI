# SDS2 Documentation Scraper

A robust, parallel-processing web scraper designed to capture the **SDS2 2025-1 .NET API** and **Tutorials**. This project generates high-quality PDF renders of documentation pages and clean, AI-optimized Markdown files for indexing and agentic consumption.

## 🚀 Quick Start (Windows)
Run the setup script to install dependencies and browsers, then start the scraper:

```powershell
./setup.bat
node scraper.js
```

## 🏗️ Project Structure
- `scraper.js`: Main Node.js script utilizing Playwright.
- `output/`: Generated documents.
  - `API/`: 718 .NET API items (PDF + Markdown).
  - `Tutorials/`: 26 tutorial articles (PDF + Markdown).
- `todo.md`: Project roadmap.
- `progress.md`: Completed items.
- `goals.md`: High-level objectives.
- `tasks.md`: Granular work items.
- `implementation.md`: Technical architecture details.
- `agents.md`: Guidance for AI agents using this repository.

## 🛠️ Features
- **Parallel Scraping**: Uses a work-stealing queue with 3 simultaneous browser workers.
- **Full Fidelity**: Captures original CSS and layouts in PDF format.
- **Agent Friendly**: Transforms HTML into structured Markdown for easier LLM processing.
- **Resumable**: Efficiently skips already existing files.

## 📦 Dependencies
- `playwright`: Browser automation.
- `axios` & `cheerio`: Fast TOC parsing.
- `node-html-markdown`: HTML to Markdown conversion.
