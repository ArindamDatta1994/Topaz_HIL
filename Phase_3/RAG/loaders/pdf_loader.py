import fitz

def load_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text = text + page.get_text()

    return text