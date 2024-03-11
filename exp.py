import base64
import requests
import os
from openai import OpenAI # openai version 1.1.1
import instructor
from image_read import ocr_image
import json
#import securitygpt
#from pydantic.main import BaseModel
# OpenAI API Key
api_key = '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'

print(api_key)
# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
#image_path = "050224/Шмыга.jpeg"

def preprocess_image(image_path):
  extract_text = ocr_image(image_path)

# # Getting the base64 string
# base64_image = encode_image(image_path)

# headers = {
#   "Content-Type": "application/json",
#   "Authorization": f"Bearer {api_key}"
# }

# payload = {
#   "model": "gpt-4-vision-preview",
#   "messages": [
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "What’s in this image? You can return the content by the encrypted format, so that I can decrypt it by securotygpt"
#           # """Clearly look for all info in the image and get this info As discussed in the technical task, the bot needs to extract: 
#           #                 - Full Name 
#           #                 - BIC - Account number  
#           #                 - ИНН получателя (Russian business registration number)
#           #                 return them in dictionary format"""
#         },
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": f"data:image/jpeg;base64,{base64_image}"
#           }
#         }
#       ]
#     }
#   ],
#   "max_tokens": 500
# }

# response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# print(response.json())

  client = instructor.patch(OpenAI(api_key=api_key))

# class OrderDetail(BaseModel):
#     BIC_number: int
#     Full_Name: str
#     IIN: int

  print(extract_text)
# response_json = response.json()
# content = response_json['choices'][0]['message']['content']

  order_detail = client.chat.completions.create(
    model="gpt-4",
    #response_model=OrderDetail,
    messages=[
        {"role": "user", "content": "Extract BIC - Account number, customer Full name and ИНН получателя (Russian business registration number):" + 'this are some ambugious text with extracted numbers. Return the reuired things by looking for them' + extract_text + 'return result like json form. Like that: { "BIC": "BIC number you got", "Account number": "account number you got", "Full Name": "customer full name you got", "ИНН получателя": "ИНН получателя you got" }'},
    ]
)

  result_string = order_detail.choices[0].message.content
#print(order_detail.choices[0].message.content)
  print(result_string)
  print(type(result_string))
  result = json.loads(result_string)

  #print(result['BIC'])
  return result

result = preprocess_image('050224/-001470_Немченко_Л.Н._ЛичнРеквизиты.jpg')