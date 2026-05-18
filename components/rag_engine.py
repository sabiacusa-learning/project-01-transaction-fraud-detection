import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

def build_rag_index(df):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    text_rows = df.apply(lambda r: f"{r['date']} {r['description']} {r['amount']} {r['merchant']}", axis=1)

    embeddings = model.encode(text_rows.tolist()).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return model, index

def retrieve(df, model, index, query, k=3):
    q_emb = model.encode([query]).astype("float32")
    _, I = index.search(q_emb, k)
    return df.iloc[I[0]]
