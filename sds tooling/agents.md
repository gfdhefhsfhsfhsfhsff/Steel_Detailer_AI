# 🤖 Agent Guidance

## 📄 Documentation Overview
This repository contains a full scrape of the **SDS2 2025-1 .NET API**. If you're an AI agent, use this guide to navigate and utilize these documents while assisting the user.

## 📂 Layout for Agents
- `output/API/`: Use this for .NET class, method, and property research.
  - Documents follow the namespace hierarchy (e.g., `DesignData.SDS2.Database.MemberHandle.md`).
- `output/Tutorials/`: Use this for context on how to perform larger tasks (e.g., "how to open a project" or "how to update a member").

## 🛠️ Usage for Common Agent Requests
- **Q: How do I create a new SDS2 project?**
  - Search `output/Tutorials/quickstart/quickstart.md`.
- **Q: What are the members of the BoltHandle class?**
  - Search `output/API/DesignData/SDS2/Database/BoltHandle/BoltHandle.md`.
- **Q: How does the licensing system work?**
  - Search `output/Tutorials/check_licensing/check_licensing.md`.

## 🧠 Strategic Tips for Agents
1. **Prefer Markdown**: While PDFs are provided for humans, the `.md` files in each folder are optimized for your context window.
2. **Namespace Search**: If a user asks about a class, use the namespace folder structure as your index.
3. **Lookup first**: Before suggesting any code, check the corresponding `.md` file to confirm parameter names and signatures.
4. **Tutorials first**: For workflow-related questions, start in the `Tutorials/` folder for better conceptual awareness.
