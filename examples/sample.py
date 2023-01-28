import os
import openai
openai.organization = "org-JCW7HsSGdQfwZzo2lZBIQLGM"
openai.api_key = 'os.getenv("OPENAI_API_KEY")'
openai.Model.list()
