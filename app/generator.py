from .config import google_api_key
from google import genai

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
      contents = user_prompt
   )
   return response.text
    

prompt = "who is current prime minister of india"
answer = generate_response(prompt)
print(answer)
        


