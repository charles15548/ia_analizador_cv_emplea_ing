from fastapi import UploadFile
from docx import Document
from PyPDF2 import PdfReader
import io

def extraer_texto(file: UploadFile) -> str:
    file.file.seek(0) 
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        return extraer_pdf(file)
    if filename.endswith(".docx"):
        return extraer_word(file)
    
    else:
        print("formato no soportado")
        raise ValueError("Formato no Soportado. Usa PDF o DOCX.")
    
def extraer_pdf(file: UploadFile) -> str:
    contenido = file.file.read()
    reader = PdfReader(io.BytesIO(contenido))

    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    return texto_limpio("\n".join(text))

def extraer_word(file: UploadFile) -> str:
    contenido = file.file.read()
    documento = Document(io.BytesIO(contenido))

    texto = [p.text for p in documento.paragraphs if p.text.strip()]
    return texto_limpio("\n".join(texto))

def texto_limpio(texto):
    texto = texto.replace("\xa0", " ")
    texto = "\n".join(line.strip() for line in texto.splitlines() if line.strip())
    return texto