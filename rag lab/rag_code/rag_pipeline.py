import os
from dotenv import load_dotenv
import openai
from rag_code.rag_prompt import build_prompt

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def query_rag(vector_db, query, k=3):
    docs = vector_db.similarity_search(query, k=k)
    prompt = build_prompt(query, docs)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
