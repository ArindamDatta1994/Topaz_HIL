import os
from loaders.pdf_loader import load_pdf
from loaders.word_loader import load_docs
from loaders.excel_loader import load_excel

from processing.chunking import chunk_text
from processing.embeddings import generate_embeddings

from vectorstore.faiss_store import FAISSStore
from retrieval.retriever import retrieve

# Step 1: Load documents
def load_all(data_path):
    texts = []

    for root, _, files in os.walk(data_path):
        for file in files:
            path = os.path.join(root, file)

            if file.endswith(".pdf"):
                texts.append(load_pdf(path))
            elif file.endswith(".docx"):
                texts.append(load_docs(path))
            elif file.endswith(".xlsx"):
                texts.append(load_excel(path))

    return texts

# Step 2: Pipeline
def build_index(texts):
    all_chunks = []

    for text in texts:
        all_chunks.extend(chunk_text(text))

    embeddings = generate_embeddings(all_chunks)

    store = FAISSStore(embeddings.shape[1])
    store.add(embeddings, all_chunks)

    return store

# Step 3: Query
def query_system(store):
    while True:
        query = input("\nEnter your query: ")
        results = retrieve(query, store)

        print("\nTop Results:")
        for r in results:
            print("-", r[:200])

# Run
if __name__ == "__main__":
    texts = load_all("data/")
    store = build_index(texts)
    query_system(store)