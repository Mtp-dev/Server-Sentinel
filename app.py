import discord
from discord.ext import commands, tasks
import mysql.connector
import requests
import json

# Bot Configuration
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
GUILD_ID = YOUR_GUILD_ID
CHANNEL_ID = YOUR_CHANNEL_ID
MC_SERVER_IP = 'your.minecraftserver.com'
MC_SERVER_PORT = 25565
MYSQL_CONFIG = {
    'host': 'your-database-host',
    'user': 'your-database-user',
    'password': 'your-database-password',
    'database': 'your-database-name'
}

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

def query_minecraft():
    """Queries the Minecraft server for player count and status."""
    try:
        response = requests.get(f'https://api.mcsrvstat.us/2/{MC_SERVER_IP}')
        data = response.json()
        return data
    except Exception as e:
        print(f"Error querying Minecraft server: {e}")
        return None

def log_to_database(tps, players):
    """Logs server data to the MySQL database."""
    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO server_logs (tps, players) VALUES (%s, %s)", (tps, players))
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as e:
        print(f"Database error: {e}")

@tasks.loop(minutes=5)
def monitor_server():
    """Checks server status and sends alerts."""
    data = query_minecraft()
    if data and data.get('online'):
        tps = data.get('debug', {}).get('tps', 'N/A')
        players = data.get('players', {}).get('online', 0)
        log_to_database(tps, players)
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            embed = discord.Embed(title='Minecraft Server Status', color=discord.Color.green())
            embed.add_field(name='TPS', value=tps, inline=True)
            embed.add_field(name='Online Players', value=players, inline=True)
            embed.set_footer(text=f'Server: {MC_SERVER_IP}')
            
            if tps != 'N/A' and float(tps) < 15.0:
                embed.color = discord.Color.red()
                embed.title = '⚠️ Server Performance Warning ⚠️'
            
            bot.loop.create_task(channel.send(embed=embed))
    else:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            bot.loop.create_task(channel.send("⚠️ The Minecraft server is down!"))

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    monitor_server.start()

@bot.command()
async def status(ctx):
    """Manually check the Minecraft server status."""
    data = query_minecraft()
    if data and data.get('online'):
        tps = data.get('debug', {}).get('tps', 'N/A')
        players = data.get('players', {}).get('online', 0)
        embed = discord.Embed(title='Minecraft Server Status', color=discord.Color.green())
        embed.add_field(name='TPS', value=tps, inline=True)
        embed.add_field(name='Online Players', value=players, inline=True)
        embed.set_footer(text=f'Server: {MC_SERVER_IP}')
        await ctx.send(embed=embed)
    else:
        await ctx.send("⚠️ The Minecraft server is offline!")

bot.run(TOKEN)
