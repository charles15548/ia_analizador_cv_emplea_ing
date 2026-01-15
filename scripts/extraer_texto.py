from fastapi import UploadFile
from docx import Document
from PyPDF2 import PdfReader
import io

def extraer_texto(file_bytes: bytes, filename: str) -> str:
    filename = filename.lower()

    if filename.endswith(".pdf"):
        return extraer_pdf_bytes(file_bytes)

    if filename.endswith(".docx"):
        return extraer_word(file_bytes)

    return ""
    
def extraer_pdf_bytes(file_bytes: bytes) -> str:
    reader = PdfReader(io.BytesIO(file_bytes))

    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)

    return texto_limpio("\n".join(text))


def extraer_word(file_bytes: bytes) -> str:
    document = Document(io.BytesIO(file_bytes))

    texto = [p.text for p in document.paragraphs if p.text.strip()]
    return texto_limpio("\n".join(texto))

def texto_limpio(texto):
    texto = texto.replace("\xa0", " ")
    texto = "\n".join(line.strip() for line in texto.splitlines() if line.strip())
    return texto