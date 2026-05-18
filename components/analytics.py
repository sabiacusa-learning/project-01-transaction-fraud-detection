
def compute_summary(df):
    total_spent = df[df['amount'] < 0]['amount'].sum()
    total_income = df[df['amount'] > 0]['amount'].sum()
    top_merchants = df['merchant'].value_counts().head(3).to_dict()
    largest_txn = df.loc[df['amount'].idxmin()].to_dict()
    fraud_signals = df[df['amount'] < -500]

    return {
        "total_spent": float(total_spent),
        "total_income": float(total_income),
        "top_merchants": top_merchants,
        "largest_transaction": largest_txn,
        "potential_fraud_transactions": fraud_signals.to_dict(orient="records")
    }, fraud_signals
