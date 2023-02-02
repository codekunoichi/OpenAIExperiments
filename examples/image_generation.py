import os
import openai
openai.organization = "org-JCW7HsSGdQfwZzo2lZBIQLGM"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="a white elephant",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)