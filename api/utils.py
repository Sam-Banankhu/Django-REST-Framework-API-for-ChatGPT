from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_KEY)
# openai.api_key = 

def send_question_to_api(question):
    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful Malawi Technical Guidelines for \
             Integrated Disease Surveilance and Response (IDSR) assistant."},
            {"role": "user", "content": f"Tell me what is {question}?"}
        ]

    )
    return res.choices[0].message.content