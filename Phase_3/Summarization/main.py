import os
from loaders.pdf_loader import load_pdf
from loaders.word_loader import load_docx
from loaders.excel_loader import load_excel

from summarizer.engine import hierarchical_summarize

def load_file(file_path = r"C:\Users\arind\All_Folders\Study\Topaz_HIL\Phase_3\Summarization\data\TheEscalatingCrisisinWestAsia.pdf"):
    if file_path.endswith(".pdf"):
        return load_pdf(file_path)
    elif file_path.endswith(".docx"):
        return load_docx(file_path)
    elif file_path.endswith(".xlsx"):
        return load_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

def main():
    file_path = r"C:\Users\arind\All_Folders\Study\Topaz_HIL\Phase_3\Summarization\data\TheEscalatingCrisisinWestAsia.pdf"

    if not os.path.exists(file_path):
        print("File not found!")
        return

    text = load_file(file_path)

    print("\nSummarizing...")

    summary = hierarchical_summarize(text)

    print("\n--- SUMMARY ---\n")
    print(summary)

if __name__ == "__main__":
    main()