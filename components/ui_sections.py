import streamlit as st

def show_summary(summary):
    st.subheader("📊 Summary Statistics")
    st.json(summary)

def show_fraud(fraud_df):
    if not fraud_df.empty:
        st.subheader("⚠️ Potential Fraud Signals")
        st.dataframe(fraud_df, use_container_width=True)
