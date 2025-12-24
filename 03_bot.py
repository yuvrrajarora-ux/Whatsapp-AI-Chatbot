import pyautogui
import time
import pyperclip   # to read clipboard text
from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI()


time.sleep(2)  # delay to switch window

# Step 1: Click on icon at (1294, 1044)
pyautogui.click(1294, 1044)
time.sleep(1)

# Step 2: Drag to select text (UPDATED COORDINATES)
pyautogui.moveTo(747, 244)
pyautogui.dragTo(1007, 958, duration=1, button='left')
time.sleep(0.5)

# Step 3: Copy
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1007, 958)
time.sleep(0.5)

# Step 4: Store in variable
chat_history = pyperclip.paste()
print("Copied Text:\n", chat_history)

prompt = (
    "You are Yuvrraj from India. You speak Hinglish (Hindi+English), "
    "you code, and you respond casually like the real chat above.\n"
    "Analyze the chat history below and reply naturally in Yuvrraj's style:\n\n"
    + chat_history +
    "\nYour reply:"
)

response = client.responses.create(
    model="gpt-5-nano",
    input=prompt
)

response = response.output_text


pyperclip.copy(response)   # copy response to clipboard

pyautogui.click(1281, 961)        # ⬅ click chat input location
time.sleep(0.3)

pyautogui.hotkey("ctrl", "v")     # paste message
time.sleep(0.2)

pyautogui.press("enter")   
