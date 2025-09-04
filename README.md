Discord Dice Bot

A Discord bot that rolls a 6-sided dice and sends a dynamically generated dice image in the chat. The dice features colored dots and smooth shadows for a polished look.

---

Features:

- Slash command /roll to roll a dice
- Generates dice images dynamically in memory
- Transparent background support
- Smooth shadowed dots
- Customizable dot colors and dice size

---

Requirements:

- Python 3.10+
- interactions.py
- Pillow

Install dependencies with:

pip install interactions.py Pillow

---

Usage:

1. Clone the repository:

git clone https://github.com/your-username/discord-dice-bot.git
cd discord-dice-bot

2. Replace BOT_TOKEN in your bot script with your Discord bot token.

3. Run the bot:

python bot.py

4. In your Discord server, type:

/tileraceroll

The bot will reply with a dice image showing the rolled number.

---

Customization:

- Dice size: Adjust the size variable (e.g., 150px, 300px)
- Dot color: Change the fill parameter in the draw.ellipse call
- Shadow: Adjust shadow_offset or Gaussian blur radius for smoother shadows

---

License:

This project is licensed under MIT License – free to use and modify. No warranty.
