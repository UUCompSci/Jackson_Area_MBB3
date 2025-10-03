import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("No API key found in environment variables!")
    exit()

client = OpenAI(api_key=api_key)

try:
    resp = client.models.list()
    print("✅ API key works! Models available:", [m.id for m in resp.data[:3]])
except Exception as e:
    print("❌ API key test failed:", e)
