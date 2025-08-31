# 🤖 Telegram Chat-Bot (Aiogram)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Aiogram](https://img.shields.io/badge/Aiogram-async-green)
![License](https://img.shields.io/badge/License-Apache_2.0-orange)

This is my **very first project** – a simple Telegram bot built with [Aiogram](https://docs.aiogram.dev/en/latest/).  
It was created for learning purposes and basic testing of Telegram bots. The code is simple and easy to extend.

---

## 🚀 Features
- 📜 `/rules` — show chat rules  
- ℹ️ `/infobot` — information about the bot  
- 🔨 `/ban` — ban a user (must be used in reply to a message)  
- 🔓 `/unban` — unban a user  
- 🛑 `/admincommand` — list of admin commands  

---

## ⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Daroya/chat-bot.git
   cd chat-bot

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Insert your bot token in main.py:
   ```bash
   bot = Bot(token="YOUR_BOT_TOKEN")

5. Run the bot:
   ```bash
   python main.py

---

## 🛠 Technologies Used
Python 3.10+
Aiogram (async framework for Telegram bots)

## 📌 Future Plans
Add inline buttons
Add /mute command
Logging to a file
Improve error handling

## 📄 License
This project is licensed under the Apache 2.0 license.
