import fitz  # PyMuPDF
import base64
from io import BytesIO
from PIL import Image
from docx import Document
import base64
from io import BytesIO

def pdf_to_images_base64(pdf_bytes: bytes) -> list[str]:
    images_base64 = []

    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

    for page in pdf:
        pix = page.get_pixmap(dpi=200)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        buffer = BytesIO()
        img.save(buffer, format="PNG")

        encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
        images_base64.append(f"data:image/png;base64,{encoded}")

    return images_base64








def docx_images_base64(docx_bytes: bytes) -> list[str]:
    images = []
    doc = Document(BytesIO(docx_bytes))

    for rel in doc.part._rels.values():
        if "image" in rel.target_ref:
            image_bytes = rel.target_part.blob
            encoded = base64.b64encode(image_bytes).decode("utf-8")
            images.append(f"data:image/png;base64,{encoded}")

    return images









