import os
import openai # pip install openai


openai.api_key = "sk-None-6kJdIcN3Cks4boP0knqLT3BlbkFJFk2MMOzQbPadG53JtDdu"

user_prompt = "cat wearing red cape"

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)