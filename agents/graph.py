from typing import TypedDict, Optional, Dict, Any
import os
from openai import AzureOpenAI
from langgraph.graph import StateGraph, END
from agents.prompts import CRITIC, DECISION, FINANCIAL, MARKET, PLANNER, STRATEGIST
from dotenv import load_dotenv

load_dotenv()


# =========================
# 🧠 State
# =========================
class GraphState(TypedDict):
    idea: str
    plan: Optional[str]

    market_analysis: Optional[str]
    financial_analysis: Optional[str]

    strategy: Optional[str]
    critique: Optional[str]

    decision: Optional[str]

    iteration: int
    max_iterations: int


# =========================
# 🤖 Azure LLM
# =========================
llm = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)


MODEL_NAME = "gpt-4o-mini"  


# =========================
# 🧭 Planner
# =========================
def planner_node(state: GraphState):
    resp = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": PLANNER},
            {"role": "user", "content": state["idea"]},
        ],
    )

    state["plan"] = resp.choices[0].message.content
    return state


# =========================
# 📊 Market Analyst
# =========================
def market_node(state: GraphState):
    resp = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": MARKET},
            {"role": "user", "content": state["idea"]},
        ],
    )

    state["market_analysis"] = resp.choices[0].message.content
    return state


# =========================
# 💰 Financial Analyst
# =========================
def financial_node(state: GraphState):
    resp = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": FINANCIAL},
            {"role": "user", "content": state["idea"]},
        ],
    )

    state["financial_analysis"] = resp.choices[0].message.content
    return state


# =========================
# ✍️ Strategist
# =========================
def strategist_node(state: GraphState):
    resp = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": STRATEGIST},
            {
                "role": "user",
                "content": f"""
Market:
{state['market_analysis']}

Financial:
{state['financial_analysis']}
""",
            },
        ],
    )

    state["strategy"] = resp.choices[0].message.content
    return state


# =========================
# 🧪 Critic
# =========================
def critic_node(state: GraphState):
    resp = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": CRITIC},
            {"role": "user", "content": state["strategy"]},
        ],
    )

    state["critique"] = resp.choices[0].message.content
    state["iteration"] += 1
    return state


# =========================
# 🏁 Decision
# =========================
def decision_node(state: GraphState):
    resp = llm.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": DECISION},
            {
                "role": "user",
                "content": f"""
Strategy:
{state['strategy']}

Critique:
{state['critique']}
""",
            },
        ],
    )

    state["decision"] = resp.choices[0].message.content
    return state


# =========================
# 🔁 Loop Logic
# =========================
def should_continue(state: GraphState):
    if state["iteration"] >= state["max_iterations"]:
        return "decision"
    return "strategist"


# =========================
# 🧩 Build Graph
# =========================
def build_graph():
    g = StateGraph(GraphState)

    g.add_node("planner", planner_node)
    g.add_node("market", market_node)
    g.add_node("financial", financial_node)
    g.add_node("strategist", strategist_node)
    g.add_node("critic", critic_node)
    g.add_node("decision", decision_node)

    g.set_entry_point("planner")

    g.add_edge("planner", "market")
    g.add_edge("market", "financial")
    g.add_edge("financial", "strategist")
    g.add_edge("strategist", "critic")

    g.add_conditional_edges("critic", should_continue)

    g.add_edge("decision", END)

    return g.compile()
