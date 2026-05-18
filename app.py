import streamlit as st

from components.file_upload import upload_csv
from components.analytics import compute_summary
from components.prompt_templates import insights_prompt, rag_prompt
from components.genai_client import get_client, ask_llm
from components.rag_engine import build_rag_index, retrieve
from components.ui_sections import show_summary, show_fraud

st.set_page_config(page_title="Banking Insights", layout="wide")
st.title("💳 Banking Insights Assistant")

df = upload_csv()

if df is not None:
    summary, fraud_df = compute_summary(df)
    show_summary(summary)

    client = get_client()

    # --- AI Insights ---
    if st.button("Generate AI Insights"):
        prompt = insights_prompt(summary)
        with st.spinner("Generating insights..."):
            output = ask_llm(client, prompt)
        st.subheader("🤖 AI Insights")
        st.write(output)
        show_fraud(fraud_df)

    # --- RAG Section ---
    st.subheader("🔍 Ask Questions About Your Transactions (RAG)")
    model, index = build_rag_index(df)

    question = st.text_input("Ask a question about your transactions")

    if question:
        retrieved_rows = retrieve(df, model, index, question)
        st.write("📌 Relevant Transactions")
        st.dataframe(retrieved_rows)

        rag_context = retrieved_rows.to_dict(orient="records")
        prompt = rag_prompt(question, rag_context)

        with st.spinner("Thinking..."):
            answer = ask_llm(client, prompt)

        st.subheader("🤖 RAG Answer")
        st.write(answer)
