import os

from groq import Groq

with open("summary_system_prompt.md", "r") as file:
    system_prompt = file.read()


def get_content_summary(content: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        max_completion_tokens=8192,
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": content,
            },
        ],
    )

    return completion.choices[0].message.content
