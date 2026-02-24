import discord
from discord.ext import commands
import asyncio
import config

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
message_id = None

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Connected to servers: {[guild.name for guild in bot.guilds]}')
    await create_role_message()

async def create_role_message():
    global message_id
    
    channel = bot.get_channel(config.CHANNEL_ID)
    if not channel:
        print("Error: Channel not found!")
        return
    
    if message_id:
        try:
            old_msg = await channel.fetch_message(message_id)
            await old_msg.delete()
        except:
            pass
    
    embed = discord.Embed(
        title="🎭 **Get Your Roles**",
        description=(
            "React to this message to get your roles:\n\n"
            "🇦 - **Role 1**\n"
            "🇧 - **Role 2**\n"
            "🇨 - **Role 3**\n\n"
            "⚠️ *Remove reaction to remove the role*"
        ),
        color=0x00ff00
    )
    embed.set_footer(text="Roles are assigned automatically")
    
    new_message = await channel.send(embed=embed)
    message_id = new_message.id
    
    for emoji in config.ROLE_MAPPING.keys():
        await new_message.add_reaction(emoji)
        await asyncio.sleep(0.5)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id:
        return
    
    await handle_reaction(payload, add_role=True)

@bot.event
async def on_raw_reaction_remove(payload):
    await handle_reaction(payload, add_role=False)

async def handle_reaction(payload, add_role: bool):
    if payload.message_id != message_id:
        return
    
    guild = bot.get_guild(payload.guild_id)
    if not guild:
        return
    
    member = guild.get_member(payload.user_id)
    if not member:
        return
    
    emoji = str(payload.emoji)
    
    if emoji not in config.ROLE_MAPPING:
        return
    
    role_id = config.ROLE_MAPPING[emoji]
    role = guild.get_role(role_id)
    
    if not role:
        print(f"Role with ID {role_id} not found!")
        return
    
    try:
        if add_role:
            if role not in member.roles:
                await member.add_roles(role)
                print(f"Added role {role.name} to {member.name}")
        else:
            if role in member.roles:
                await member.remove_roles(role)
                print(f"Removed role {role.name} from {member.name}")
    except discord.Forbidden:
        print("Bot doesn't have permission to manage roles!")
    except Exception as e:
        print(f"Error: {e}")

@bot.command(name='update_roles')
@commands.has_permissions(administrator=True)
async def update_roles(ctx):
    await create_role_message()
    await ctx.send("Role message updated!", delete_after=5)

if __name__ == "__main__":
    if config.TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("Error: Please set your bot token in config.py!")
    else:
        bot.run(config.TOKEN)
