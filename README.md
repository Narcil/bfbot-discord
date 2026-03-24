# bfbot-discord

A modular Discord bot powered by **discord.py** and **LangChain**. This bot allows users to interact with local or API-based AI models, providing intelligent conversational capabilities and utility tools directly within Discord channels.

## 🚀 Features

The bot is built using **Cogs**, allowing for easy toggling of features. Below are the primary modules included:

### 🧠 AI & Chat (LangChain Integration)
* **Contextual Conversations:** Remembers previous messages in a thread for natural, back-and-forth dialogue.
* **Local LLM Support:** Optimized to work with local AI instances (like Ollama or LocalAI) to keep your data private.
* **Prompt Templates:** Uses structured templates to ensure the AI follows specific personas or rules.

### 🛠️ Utility Cogs
* **System Monitoring:** Check the bot's latency (ping) and uptime.
* **Admin Tools:** Commands for reloading cogs on the fly without restarting the entire bot process.
* **Logging:** Detailed console logging for tracking AI queries and Discord interactions.

---

## 📋 Requirements

* **Python 3.10+**
* **Discord Bot Token** (via [Discord Developer Portal](https://discord.com/developers/applications))
* **AI Backend:** An API key (OpenAI, Anthropic) or a local provider (Ollama) running on your machine.

---

## 🛠️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Narcil/bfbot-discord.git
    cd bfbot-discord
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your credentials:
    ```env
    DISCORD_TOKEN=your_token_here
    AI_API_KEY=your_key_here
    BASE_URL=http://localhost:11434  # If using Ollama/LocalAI
    ```

4.  **Run the Bot:**
    ```bash
    python main.py
    ```

---

## ⌨️ Commands

| Command | Description |
| :--- | :--- |
| `!ask [question]` | Sends a prompt to the AI and returns the response. |
| `!clear` | Clears the current conversation context for the user. |
| `!ping` | Returns the bot's current heartbeat latency. |
| `!reload [cog]` | (Admin only) Reloads a specific feature module. |

---

## 🧩 Project Structure

```text
bfbot-discord/
├── cogs/               # Feature modules (AI, Utils, etc.)
├── utils/              # Helper functions and wrappers
├── main.py             # Bot entry point
└── requirements.txt    # Python dependencies
```

---

**License:** This project is licensed under the MIT License.

---
