from PyPDF2 import PdfReader

def read_pdf(path):
    text = ""
    reader = PdfReader(path)

    for page in reader.pages:
        try:
            content = page.extract_text()
            print("PDF CONTENT:", content)
            if content:
                text += content
        except:
            continue

    return text.strip()