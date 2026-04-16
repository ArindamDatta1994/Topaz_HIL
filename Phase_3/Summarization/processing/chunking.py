def chunk_text(text, chunk_size = 400):
    words = text.split()
    chunk = []

    for i in range(0, len(words), chunk_size):
        chunk.append(" ".join(words[i:i + chunk_size]))

    return chunk