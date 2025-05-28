from .config import google_api_key
from prompts.sysprompt import sys_prompt
from google import genai
from google.genai import types

try:
   client = genai.Client(
    api_key= google_api_key,
    vertexai=False
    )
except:
   print("this is a problem with generator client")

def generate_response(user_prompt):
   response = client.models.generate_content(
      model = "gemini-2.0-flash",
      config= types.GenerateContentConfig(
         system_instruction= sys_prompt
      ),
      contents = user_prompt
   )
   return response.text
    

# prompt = "generate 5 question on geometry"
# answer = generate_response(prompt)
# print(answer)



