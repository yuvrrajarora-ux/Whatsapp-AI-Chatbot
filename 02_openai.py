import os
from openai import OpenAI

# Set your API key via environment variable or directly here
os.environ["OPENAI_API_KEY"] = "ENTER_YOUR_API_KEY_HERE"

client = OpenAI()

# Paste chat history here
command = '''
<PASTE_CHAT_HISTORY_HERE>
'''

# Generic, privacy-safe prompt
prompt = (
    "You are a friendly and natural conversational chatbot. "
    "Read the chat history below and generate the next reply in a casual, human-like tone. "
    "The reply should feel natural, short if needed, and appropriate to the context.\n\n"
    + command +
    "\nYour reply:"
)

response = client.responses.create(
    model="gpt-5-nano",
    input=prompt
)

print(response.output_text)
