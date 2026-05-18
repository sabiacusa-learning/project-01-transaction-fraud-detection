

def insights_prompt(summary):
    return f"""
    You are an AI banking analyst. Based on this transaction summary:

    {summary}

    Provide:
    1. Spending behavior analysis
    2. Potential fraud indicators
    3. Recommendations for the customer
    4. A short banker-friendly summary
    """

def rag_prompt(question, context):
    return f"""
    The user asked: "{question}"

    Here are the most relevant transactions:
    {context}

    Use ONLY this data to answer.
    """
