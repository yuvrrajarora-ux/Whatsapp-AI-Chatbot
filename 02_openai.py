import os
from openai import OpenAI

# Put your API key here like ↓ (inside quotes) or set via environment variable
os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI()

command =  '''
[8:50 pm, 28/11/2025] Shampy: 1
[8:50 pm, 28/11/2025] Shampy: 2
[8:50 pm, 28/11/2025] Shampy: 3
[8:50 pm, 28/11/2025] Yuvrraj Arora: abe
[8:50 pm, 28/11/2025] Yuvrraj Arora: kuch question puchiyo
[8:50 pm, 28/11/2025] Yuvrraj Arora: maine darasal codewithharry se dekh kar whatsaap chatbot bnya
[8:50 pm, 28/11/2025] Shampy: Achaaa
[8:50 pm, 28/11/2025] Yuvrraj Arora: kuch puchiyo mere se
[8:50 pm, 28/11/2025] Shampy: Hey how are you
[8:50 pm, 28/11/2025] Shampy: How's the weather today
[8:53 pm, 28/11/2025] Shampy: How's the weather
'''

prompt = (
    "You are Yuvrraj from India. You speak Hinglish (Hindi+English) naturally like a real person, "
    "not like an AI. You talk casual, friendly, emotional and relatable — just like normal chat.\n"
    "You read the chat history below exactly how a real WhatsApp conversation feels and then reply "
    "as Yuvrraj would — natural, spontaneous, unfiltered, human.\n"
    "Output should be the NEXT message in the chat written as Yuvrraj.\n"
    "Let the message feel real — short if needed, sometimes expressive, sometimes funny, sometimes deep.\n\n"
    + command +
    "\nYour reply:"
)

response = client.responses.create(
    model="gpt-5-nano",
    input=prompt
)

print(response.output_text)
