import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()
api_key= os.getenv('API_KEY')
client= OpenAI(api_key=api_key)

# code for image description generator for web image
# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {"type": "text", "text": "What’s in this image?"},
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
#           },
#         },
#       ],
#     }
#   ],
#   max_tokens=300,
# )

# print(response.choices[0])


# code for generating image description for image from local machine
# def image_to_base64(image_path): 
#     with open(image_path,"rb") as image_file: 
#         encoded_string= base64.b64encode(image_file.read())
#         return encoded_string.decode("utf-8")

# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {
#         "role":"system",
#         "content":[
#             {
#                 "type":"text",
#                 "text":"Return a JSON structure based on the requirements of user. Only return the JSON structure, nothing else. Donot return ```json"
#             }
#         ]
#     },
#     {
#       "role": "user",
#       "content": [
#         {
#             "type": "text",
#             "text": "Create a JSON structure for all the items in the image. Return only the JSON structure."
#         },
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": f"data:image/png;base64,{image_to_base64('beach.png')}"
#           },
#         },
#       ],
#     }
#   ],
#   max_tokens=300,
# )


# code for generating description for multiple images
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
        "role":"system",
        "content":[
            {
                "type":"text",
                "text":"Return a JSON structure based on the requirements of user. Only return the JSON structure, nothing else. Donot return ```json"
            }
        ]
    },    
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What are in these images? Is there any difference between them? return the answer in JSON format only, nothing else",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://i.postimg.cc/D0C66v2f/beach.png",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

# description generation with low and high fidelity of images

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
        "role":"system",
        "content":[
            {
                "type":"text",
                "text":"Return a JSON structure based on the requirements of user. Only return the JSON structure, nothing else. Donot return ```json"
            }
        ]
    },
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image? return the answer in JSON format only, nothing else"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            "detail": "low"
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)