from processing.embeddings import model

def retrieve(query, vector_store, k = 2):
    query_embedding = model.encode([query])
    result, distances = vector_store.search(query_embedding, k)

    return result