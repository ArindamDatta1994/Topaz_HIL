def answer_query(query, retrieved_chunks):
    context = " ".join(retrieved_chunks)

    prompt = f"""
    Answer the question based on context:

    Context: {context}
    Question: {query}
    """

    # Replace with your LLM (Groq/OpenAI)
    return prompt