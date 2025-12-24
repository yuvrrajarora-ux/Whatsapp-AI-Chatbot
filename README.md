# Whatsapp-AI-Chatbot
A Python-based WhatsApp chatbot that reads desktop chat history, generates human-like replies using AI, and automatically sends responses using GUI automation.
This project demonstrates how AI, clipboard handling, and desktop automation can be combined to simulate a real-time chat assistant.

# Features

1. Reads WhatsApp chat history from the screen
2. Uses AI to generate human-like replies
3. Supports Hinglish casual conversation style
4. Automatically pastes and sends replies
5. Fully desktop-based automation (no WhatsApp API required)
6. Simple and modular script structure

# Tech Stack

1. Python
2. OpenAI API
3. PyAutoGUI
4. Pyperclip
5. OS environment variables


# Whatsapp-ai-chatbot/
│
├── 01_get_cursor.py      # Utility to find screen coordinates
├── 02_openai.py          # Test script for AI responses
├── 03_bot.py             # Main WhatsApp automation bot
└── README.md             # Documentation

# How It Works

1. The bot clicks on WhatsApp Desktop using fixed screen coordinates.
2. It selects and copies the chat text from the screen.
3. The copied text is sent to the AI model as context.
4. The AI generates a natural reply.
5. The reply is pasted back into WhatsApp and sent automatically.

# Setup
1. Install dependencies
pip install pyautogui pyperclip openai

2. Add your OpenAI API key
Inside the code:
os.environ["OPENAI_API_KEY"] = "ENTER_YOUR_API_KEY_HERE"

# Usage

1. Open WhatsApp Desktop.
2. Adjust screen coordinates using 01_get_cursor.py.
3. Update coordinates in 03_bot.py.
4. Run the bot:
python 03_bot.py

The bot will read the current chat and reply automatically.

# Limitations

1. Screen resolution dependent (coordinates must be adjusted per device)
2. Requires WhatsApp Desktop open and visible
3. Internet connection required for AI
4. Not an official WhatsApp integration

# Disclaimer
This project uses screen automation and is not affiliated with WhatsApp or Meta.
It is intended for educational and experimental purposes only.

Author
Yuvrraj Arora
