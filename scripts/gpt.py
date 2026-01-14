import os
import openai
from dotenv import load_dotenv
from scripts.promps import promt_base
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
from openai import OpenAI
client = OpenAI()


# def llamada_gpt(cv_text):

#     response = client.responses.create(
#         model = "gpt-5.1",
#         input= promt_base(cv_text)

#     )
#     return response.output_text

# def llamada_gpt(cv_text):

#     response = client.responses.create(
#         model="gpt-5.1",
#         input=promt_base(cv_text)
#     )

#     output_text = ""

#     for item in response.output:
#         if item.type == "output_text":
#             output_text += item.text

#     if not output_text:
#         raise ValueError("GPT no devolvió texto")
    
#     print(output_text)

#     return output_text



def llamada_gpt(cv_text,images):
    content = [
        {
            "type": "input_text",
            "text": promt_base(cv_text)
        }
    ]
    for img in images:
        content.append({
            "type": "input_image",
            "image_url": img
        })


    response = client.responses.create(
        model="gpt-5.1",
        input=[
            {
                "role": "user",
                "content": content
            }
        ]
    )

    output_text = ""

    for item in response.output:
        # Caso más común en GPT-5.x
        if hasattr(item, "content"):
            for content in item.content:
                if hasattr(content, "text") and content.text:
                    output_text += content.text


    if not output_text.strip():
        raise ValueError("GPT no devolvió texto usable")

    return output_text.strip()
