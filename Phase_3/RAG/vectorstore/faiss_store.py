import faiss
import numpy as np

class FAISSStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.text_chunk = []

    def add(self, embeddings, chunks):
        self.index.add(np.array(embeddings))
        self.text_chunk.extend(chunks)

    def search(self, query_embedding, k = 5):
        distance, indices = self.index.search(query_embedding, k)
        results = [self.text_chunk[i] for i in indices[0]]
        return results, distance[0]