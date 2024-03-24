from PyPDF2 import PdfReader

def load_split_pdf(pdf_path):
    pdf_loader = PdfReader(open(pdf_path, "rb"))
    pdf_text = ""
    for page_num in range(len(pdf_loader.pages)):
        pdf_page = pdf_loader.pages[page_num]
        pdf_text += pdf_page.extract_text()
    return pdf_text.replace("\n", " ")

