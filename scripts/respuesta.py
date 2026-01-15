from scripts.extraer_texto import extraer_texto
from scripts.extraer_img import pdf_to_images_base64

import json
from scripts.gpt import llamada_gpt
def respuesta(file,puesto):
    file.file.seek(0)
    file_bytes = file.file.read()

    cv_text = extraer_texto(file_bytes, file.filename)
    
    print("\n===== TEXTO EXTRAÍDO =====")
    print(cv_text[:1000])  # solo los primeros 1000 caracteres
    print("\n===== FIN TEXTO =====")


    images = []
    filename = file.filename.lower()

    


    if filename.endswith(".docx"):
       
        images = pdf_to_images_base64(file_bytes)
    elif filename.endswith(".pdf"):
        images = pdf_to_images_base64(file_bytes)

    if not cv_text.strip():
        cv_text = (
            "El CV no contiene texto legible. "
            "Analiza únicamente a partir del contenido visual."
        )

    response = llamada_gpt(cv_text,images,puesto)
    

    print("\n===== RESPUESTA GPT =====")
    print(response[:1300])  # solo los primeros 1000 caracteres
    print("\n===== FIN GPT =====")

    resultado = json.loads(response)
    return resultado
