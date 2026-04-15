import streamlit as st
from agents.graph import build_graph

st.set_page_config(page_title="AI Startup Advisor", layout="wide")

st.title("🚀 AI Startup Decision System")

idea = st.text_area("💡 Enter your startup idea:")

if st.button("Analyze"):
    app = build_graph()

    with st.spinner("🤖 AI is analyzing your idea..."):
        result = app.invoke({
            "idea": idea,
            "iteration": 0,
            "max_iterations": 2
        })

    # ======================
    # 🎯 Decision Badge
    # ======================
    decision_text = result["decision"]

    if "GO" in decision_text.upper():
        st.success("🟢 GO")
    else:
        st.error("🔴 NO-GO")

    st.subheader("📊 Final Decision")
    st.write(decision_text)

    # ======================
    # 📂 Tabs
    # ======================
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🧭 Plan",
        "📊 Market",
        "💰 Financial",
        "✍️ Strategy",
        "🧪 Critique"
    ])

    with tab1:
        st.write(result.get("plan", "No data"))

    with tab2:
        st.write(result.get("market_analysis", "No data"))

    with tab3:
        st.write(result.get("financial_analysis", "No data"))

    with tab4:
        st.write(result.get("strategy", "No data"))

    with tab5:
        st.write(result.get("critique", "No data"))