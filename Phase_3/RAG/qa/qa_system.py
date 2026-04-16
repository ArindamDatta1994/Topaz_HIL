from qa.llm_client import generate_response

def answer_query(query, retrieved_chunks):
    context = "\n".join(retrieved_chunks)

    prompt = f"""
You are a question-answering system.

Use ONLY the context below to answer the question.
If the answer is not in the context, say "I don't know."

Context:
{context}

Question:
{query}

Answer:
"""

    return generate_response(prompt)