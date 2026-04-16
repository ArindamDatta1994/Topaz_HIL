from docx import Document

def load_docs(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])