import pyautogui
import time
import pyperclip
from openai import OpenAI
import os

# Set your API key via environment variable or replace this placeholder locally
os.environ["OPENAI_API_KEY"] = "ENTER_YOUR_API_KEY_HERE"

client = OpenAI()

time.sleep(2)  # delay to switch window

# Step 1: Click on WhatsApp icon (update coordinates as needed)
pyautogui.click(1294, 1044)
time.sleep(1)

# Step 2: Drag to select chat text
pyautogui.moveTo(747, 244)
pyautogui.dragTo(1007, 958, duration=1, button='left')
time.sleep(0.5)

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1007, 958)
time.sleep(0.5)

# Step 4: Store copied chat
chat_history = pyperclip.paste()
print("Copied Text:\n", chat_history)

# Generic, privacy-safe prompt
prompt = (
    "You are a friendly and natural conversational chatbot. "
    "Read the chat history below and generate the next reply in a casual, human-like tone. "
    "The reply should be appropriate, concise, and context-aware.\n\n"
    + chat_history +
    "\nYour reply:"
)

response = client.responses.create(
    model="gpt-5-nano",
    input=prompt
)

response = response.output_text

# Copy AI response back to clipboard
pyperclip.copy(response)

# Step 5: Paste and send reply
pyautogui.click(1281, 961)  # chat input box
time.sleep(0.3)

pyautogui.hotkey("ctrl", "v")
time.sleep(0.2)

pyautogui.press("enter")
