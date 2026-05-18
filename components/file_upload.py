import pandas as pd
import streamlit as st

def upload_csv():
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("📄 Raw Transactions")
        st.dataframe(df, use_container_width=True)
        return df
    return None
