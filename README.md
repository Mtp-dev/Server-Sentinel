```markdown
# Server Sentinel - Minecraft Server Monitor Bot

Server Sentinel is a Discord bot designed to monitor a Minecraft server, log performance metrics to a MySQL database, and notify Discord channels of server status changes and performance issues.

## Features
- ✅ Automatically monitors Minecraft server uptime, TPS, and player count.
- ⚠️ Sends alerts to Discord when the server is down or TPS is low.
- 🗂️ Logs server performance data in a MySQL database for analysis.
- 📊 Allows admins to check server status with a Discord command.

## Requirements
- Python 3.8+
- A running Minecraft server
- A Discord bot token
- A MySQL database
- `mcsrvstat.us` API for server status

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/mtp-dev/server-sentinel.git
   cd server-sentinel
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure your bot settings in the script:
   - Replace `YOUR_DISCORD_BOT_TOKEN` with your Discord bot token.
   - Replace `YOUR_GUILD_ID` and `YOUR_CHANNEL_ID` with your Discord server and channel IDs.
   - Set `MC_SERVER_IP` to your Minecraft server address.
   - Configure `MYSQL_CONFIG` with your MySQL database details.

4. Run the bot:
   ```sh
   python server_sentinel.py
   ```

## Commands
| Command | Description |
|---------|-------------|
| `!status` | Checks and displays the current Minecraft server status. |

## MySQL Database Setup
Run the following SQL command to create the required table:
```sql
CREATE TABLE server_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tps FLOAT,
    players INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Contributing
Pull requests are welcome. For major changes, open an issue first to discuss proposed improvements.

## License
This project is licensed under the MIT License.
```
