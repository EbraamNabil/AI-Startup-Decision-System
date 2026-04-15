# 🚀 AI Startup Decision System

An intelligent multi-agent system that analyzes startup ideas and provides a clear, data-driven **GO / NO-GO decision** using AI.

---

## 🧠 Overview

Building a startup is risky. Many founders rely on intuition instead of structured analysis.

This project solves that problem by simulating a **team of AI experts** that collaborate to evaluate any startup idea — just like a real-world startup advisory board.

---

## ⚙️ How It Works

The system is built using a **multi-agent architecture** powered by Azure OpenAI and LangGraph.

Each agent has a specific role:

### 🧭 Planner

Breaks down the idea into actionable analysis steps.

### 📊 Market Analyst

Evaluates:

* Market demand
* Target audience
* Competitive landscape

### 💰 Financial Analyst

Estimates:

* Initial cost
* Monthly expenses
* Revenue potential
* Break-even timeline

### ✍️ Strategist

Combines all insights into a structured recommendation.

### 🧪 Critic

Reviews the output for:

* Weak reasoning
* Missing points
* Overconfidence

### 🏁 Decision Engine

Delivers:

* Final verdict (**GO / NO-GO**)
* Explanation
* Confidence score

---

## 🔁 Iterative Intelligence

The system includes a **self-improvement loop**:

1. Generate strategy
2. Critique it
3. Improve it
4. Repeat until quality threshold

This makes the output significantly more reliable than a single-pass AI response.

---

## 🎨 Features

* ✅ Multi-agent collaboration
* 🔁 Iterative refinement loop
* 📊 Financial estimation with realistic numbers
* 🧠 Explainable AI (see each step)
* 🟢 Clear GO / NO-GO decision
* 💻 Interactive UI using Streamlit

---

## 🖥️ Demo UI

The interface provides:

* Input field for startup idea
* Decision badge (GO / NO-GO)
* Tabs for each agent:

  * Plan
  * Market Analysis
  * Financial Analysis
  * Strategy
  * Critique

---

## 🛠️ Tech Stack

* Python
* Azure OpenAI
* LangGraph
* Streamlit
* Pydantic
* dotenv

---

## 📦 Project Structure

```
my_project/
│
├── agents/
│   ├── graph.py
│   ├── prompts.py
│   └── __init__.py
│
├── streamlit_app.py
├── .env
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-startup-decision-system.git
cd ai-startup-decision-system
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file in the root folder:

```env
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
```

---

### 5. Run the application

```bash
streamlit run streamlit_app.py
```

---

### 6. Open in browser

```
http://localhost:8501
```

---

## 🧪 Example Use Cases

Try inputs like:

* "SaaS platform for gym management"
* "Food delivery app in a small town"
* "AI-powered customer support tool"

---

## 📊 Example Output

```
GO

Strong demand in urban markets.
Moderate competition.
Break-even expected within 6 months.

Confidence: 82%
```

---

## 💡 Why This Project Matters

This is not just a chatbot.

It demonstrates:

* Multi-agent AI systems
* Decision-making pipelines
* Iterative reasoning
* Real-world business logic

---

## 🏆 Future Improvements

* 🔌 Integration with real market APIs
* 📈 More accurate financial modeling
* 🧠 Memory & context persistence
* 🌍 Deployment (Streamlit Cloud / Docker)

---

## 👨‍💻 Author

Built with a focus on real-world AI systems and production-ready architecture.

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!
