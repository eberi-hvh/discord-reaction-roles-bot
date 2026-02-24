# discord-reaction-roles-bot
A powerful and easy-to-use Discord bot that lets users self-assign roles by reacting to messages. Perfect for gaming communities, study groups, or any server that needs organized role management.

✨ Features
Instant Role Assignment - Users get roles immediately after reacting

Toggle System - Remove reaction = remove role

Beautiful Embeds - Clean and customizable messages

Multi-Role Support - Unlimited roles and emojis

Admin Commands - Easy management for server administrators

📸 Preview
text
_________________________________________________
|  🎭 Get Your Roles                            |
|                                               |
|  React to this message to get your roles:     |
|                                               |
|  🇦 - Gamer                                    |
|  🇧 - Streamer                                 |
|  🇨 - Announcements                            |
|                                               |
|  ⚠️ Remove reaction to remove the role        |
|_______________________________________________|
🚀 Quick Start
Prerequisites
Python 3.8 or higher

Discord Bot Token (Get it here)

Discord server with administrator access

Installation in 3 Steps
Clone the repository


git clone https://github.com/eberi-hvh/discord-reaction-roles-bot.git
cd discord-reaction-roles-bot
Install dependencies


pip install -r requirements.txt
Configure and run


# Edit config.py with your bot token and IDs
python bot.py
⚙️ Configuration
Edit config.py:

python
TOKEN = "YOUR_BOT_TOKEN"           # Your bot token
CHANNEL_ID = 1234567890             # Channel for roles message

# Map emojis to role IDs
ROLE_MAPPING = {
    "🇦": 1234567890,  # Gamers role
    "🇧": 1234567890,  # Streamers role
    "🇨": 1234567890,  # Announcements role
}
📖 Commands
Command	Description	Permission
!update_roles	Refresh the role selection message	Administrator only
🔧 Bot Permissions Required
✅ Manage Roles

✅ Read Messages

✅ Send Messages

✅ Add Reactions

✅ Read Message History

✅ Embed Links

🏗️ Project Structure
text
discord-reaction-roles-bot/
├── bot.py              # Main bot code
├── config.py           # Configuration file
├── requirements.txt    # Dependencies
└── README.md          # Documentation
🎯 Use Cases
Gaming Servers - Let players choose their favorite games

Study Groups - Assign roles for different subjects

Communities - Give users control over their notifications

Event Planning - Separate organizers from attendees

Support Servers - Distinguish between users and staff

🤝 Contributing
Contributions are welcome!

Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Open a Pull Request

📝 License
Distributed under the MIT License.
