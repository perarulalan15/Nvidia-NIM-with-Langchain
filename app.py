from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
from dotenv import load_dotenv
load_dotenv()


client = ChatNVIDIA(
  model="tiiuae/falcon3-7b-instruct",
  api_key=os.getenv("FALCON_KEY"), 
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
)

for chunk in client.stream([{"role":"user","content":"provide a brief overview of the history of artificial intelligence"}]): 
  print(chunk.content, end="")