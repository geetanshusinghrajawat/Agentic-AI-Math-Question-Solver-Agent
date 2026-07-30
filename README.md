# 🧮 AI Math Problem Solver (LLM Agent)

An agentic AI application that solves mathematical problems using natural language — powered by LLaMA 3.1, LangChain agents, and a multi-tool architecture including a calculator, reasoning engine, and web search.

## 🚀 Live Demo
[**Try it here →**]([your-streamlit-link](https://agentic-ai-math-question-solver-agent-by-geetanshu.streamlit.app/))

## 📌 Overview

Type any math problem in plain English and the agent figures out how to solve it. It routes your question to the right tool — arithmetic goes to the calculator, logic problems go to the reasoning engine, and factual questions trigger a web search. Built on a Zero-Shot ReAct agent that decides tool usage autonomously.

## 🛠️ How It Works

1. **Input** — User enters a math or reasoning question in natural language
2. **Routing** — A regex check routes pure arithmetic directly to the calculator; everything else goes to the ReAct agent
3. **Agent** — Zero-Shot ReAct agent (LLaMA 3.1 via Groq) decides which tool to use based on the question
4. **Tools**:
   - 🔢 **Calculator** — `LLMMathChain` extracts and evaluates mathematical expressions
   - 🧠 **Reasoning Tool** — `LLMChain` with a custom prompt for logic and word problems; replies with step-by-step point-wise solutions
   - 🔍 **Search Tool** — `DuckDuckGoSearchRun` for factual/general knowledge queries
5. **Memory** — Chat history maintained in Streamlit session state across the conversation
6. **Deployment** — Streamlit app with sidebar API key input and chat-style interface

## 🧰 Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| LLM | LLaMA 3.1 8B Instant (via Groq API) |
| Framework | LangChain |
| Agent Type | Zero-Shot ReAct |
| Tools | LLMMathChain, LLMChain, DuckDuckGoSearchRun |
| Deployment | Streamlit |

## 📁 Project Structure

```
├── AI_Math_Solver.py    # Main Streamlit app with agent and tools
├── .env                 # API keys (not committed)
└── requirements.txt     # Dependencies
```

## ⚙️ Run Locally

```bash
# Clone the repo
git clone https://github.com/geetanshusinghrajawat/your-repo-name
cd your-repo-name

# Install dependencies
pip install langchain langchain-groq langchain-community streamlit python-dotenv duckduckgo-search

# Run the app
streamlit run AI_Math_Solver.py
```

> **Note:** You'll be prompted to enter your Groq API Key in the app sidebar — no `.env` file needed for local testing.

## 🔑 Getting API Keys

- **Groq API Key** — Free at [console.groq.com](https://console.groq.com)

## ✨ Features

- 🧮 Solves arithmetic, algebra, and numerical problems
- 🧠 Handles logic and reasoning questions with step-by-step answers
- 🔍 Falls back to web search for factual queries
- 💬 Chat-style interface with conversation history
- 🚫 Gracefully rejects non-math questions with a clear message
- ⚡ Fast inference via Groq's LPU hardware

## 👤 Author

**Geetanshu Singh Rajawat**  
[LinkedIn](https://www.linkedin.com/in/geetanshu-singh-rajawat/) | [GitHub](https://github.com/geetanshusinghrajawat)
