from processing.chunking import chunk_text
from processing.cleaner import clean_text
from summarizer.model import summarize_text

def summarize_document(text):
    text = clean_text(text)
    chunks = chunk_text(text)

    summarise = []

    for chunk in chunks:
        summary = summarize_text(chunk)
        summarise.append(summary)

    return " ".join(summarise)

def hierarchical_summarize(text):
    text = clean_text(text)
    chunks = chunk_text(text)

    level1 = [summarize_text(c) for c in chunks]

    combined = " ".join(level1)

    final_summary = summarize_text(combined)

    return final_summary