import pymupdf

def pdf_to_txt(pdf_path):
    """Extracts text from a PDF """
    doc = pymupdf.open(pdf_path)
    text = "\n".join(page.get_text() for page in doc)  # Extracts text from all pages

    return text  # Returns the extracted text