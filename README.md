# 🧠 Memory AI Assistant

An AI assistant built with **Python, Gemini, Streamlit, and JSON-based persistent memory**.

This project demonstrates how an AI assistant can maintain both **short-term conversation context** and **long-term memory** across conversations.

---

## ✨ Features

- 💬 Interactive Streamlit chat interface
- 🧠 Short-term conversation memory
- 💾 Persistent long-term memory using JSON
- 🔄 Memory retrieval across new conversations
- ➕ Save important information to long-term memory
- 🗑️ Delete individual memories
- 🧹 Delete all stored memories
- 🔄 Clear current conversation
- 🤖 Gemini-powered AI responses
- 🔐 API key stored securely using environment variables
- 📁 Simple and lightweight file-based architecture

---

## 🏗️ How Memory Works

The assistant uses two types of memory.

### 1. Short-Term Memory

Short-term memory stores messages from the current conversation.

Example:

```text
User: My favorite subject is Artificial Intelligence.

User: What is my favorite subject?

Assistant: Your favorite subject is Artificial Intelligence.
```

### 2. Long-Term Memory

Important information can be explicitly saved using commands such as:

```text
Remember that I am learning Python for AI development.
```

The information is stored persistently in:

```text
memories.json
```

It can be retrieved after the current conversation is cleared or restarted.

Example:

```text
User: What am I learning for AI development?

Assistant: You are learning Python for AI development.
```

---

## 🛠️ Technologies Used

- **Python**
- **Google Gemini API**
- **Google GenAI SDK**
- **Streamlit**
- **python-dotenv**
- **JSON**

---

## 📂 Project Structure

```text
ai-agent-memory/
│
├── app.py
├── memory.py
├── memories.json
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
└── screenshots/
    ├── 01_chat_short_term_memory.png
    ├── 02_long_term_memory_saved.png
    ├── 03_memory_retrieved_new_conversation.png
    └── 04_memory_deleted.png
```

> `.env` contains the Gemini API key and must not be uploaded to GitHub.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ai-agent-memory
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in the browser.

---

## 🧪 Example Tests

### Test 1 — Short-Term Memory

```text
User: My favorite subject is Artificial Intelligence.

User: What is my favorite subject?
```

Expected result:

```text
Artificial Intelligence
```

### Test 2 — Save Long-Term Memory

```text
User: Remember that I am learning Python for AI development.
```

The information is saved to persistent memory.

### Test 3 — Retrieve Long-Term Memory

After clearing the current conversation:

```text
User: What am I learning for AI development?
```

Expected result:

```text
You are learning Python for AI development.
```

### Test 4 — Memory Management

The sidebar provides controls for:

- Viewing stored memories
- Deleting an individual memory
- Deleting all memories
- Clearing the current conversation

---

## 🧠 Memory Management

Stored memories are represented as JSON objects containing an ID, memory content, and creation timestamp.

Example:

```json
{
  "id": 1,
  "content": "I am learning Python for AI development.",
  "created_at": "2026-10-08 00:00:00"
}
```

The memory system provides functions for:

- Adding memories
- Loading memories
- Retrieving memories
- Deleting individual memories
- Clearing all memories
- Managing current conversation history

---

## 🔐 Security

The Gemini API key is stored in the `.env` file.

The `.env` file is included in `.gitignore` and should **never be committed to GitHub**.

Never expose the API key in:

- `app.py`
- `README.md`
- screenshots
- source code
- GitHub commits

---

## 📸 Project Screenshots

The project includes screenshots demonstrating the required functionality:

1. **Short-Term Conversation Memory**
2. **Long-Term Memory Saved**
3. **Memory Retrieved in a New Conversation**
4. **Memory Deleted**

---

## 🎯 Learning Objectives

This project demonstrates:

1. How AI assistants maintain conversation state.
2. The difference between short-term and long-term memory.
3. How persistent memory can be stored locally.
4. How previous information can be retrieved in future conversations.
5. How users can manage and delete stored memories.
6. How an LLM can be integrated into a stateful application.

---

## 🚀 Future Improvements

Possible improvements include:

- Semantic memory search
- Vector database integration
- Automatic memory extraction
- Memory importance scoring
- Multiple user profiles
- Conversation history persistence
- Memory summarization
- Advanced memory retrieval

---

## 👩‍💻 Project

**AI Agent Memory and Conversation State**

Built as part of an AI/GenAI learning project.
