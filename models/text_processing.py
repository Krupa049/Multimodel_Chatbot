from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_KEY")

def process_text(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content