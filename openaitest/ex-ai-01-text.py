from openai import OpenAI
import os

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "이순신의 업적 5가지"
        }
    ]
)

print(completion.choices[0].message.content)