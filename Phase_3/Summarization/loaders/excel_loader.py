import pandas as pd

def load_excel(file_path):
    text = ""
    xls = pd.ExcelFile(file_path)

    for sheet in xls.sheet_names:
        df = xls.parse(sheet)
        text = text + df.to_string()

    return text