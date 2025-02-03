# 🛡️ Server Sentinel - Minecraft Server Monitor Bot

Server Sentinel is a Discord bot that monitors a Minecraft server’s uptime, TPS, and player count, logs performance data to a MySQL database, and sends alerts to a Discord channel when issues arise.

## 🚀 Features
✅ **Automatic Monitoring** - Tracks Minecraft server uptime, TPS, and player count every 5 minutes.  
⚠️ **Alerts & Notifications** - Sends alerts if the server is down or TPS drops below a safe threshold.  
🗂️ **MySQL Data Logging** - Stores performance metrics for historical analysis.  
📊 **Admin Commands** - Allows manual status checks via Discord commands.  

---

## 🛠️ Requirements
- **Python 3.8+**
- **Minecraft Server** (Java Edition)
- **Discord Bot Token**
- **MySQL Database**
- **`mcsrvstat.us` API** (Used for fetching server status)

---

## 🔧 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/mtp-dev/server-sentinel.git
cd server-sentinel
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Configure the Bot
Edit the `server_sentinel.py` file and update the following:

- Replace `YOUR_DISCORD_BOT_TOKEN` with your bot’s token.
- Replace `YOUR_GUILD_ID` and `YOUR_CHANNEL_ID` with the correct Discord server and channel IDs.
- Set `MC_SERVER_IP` to your Minecraft server address.
- Update `MYSQL_CONFIG` with your MySQL database credentials.

### 4️⃣ Run the Bot
```sh
python server_sentinel.py
```

---

## 🔹 Discord Commands

| Command  | Description |
|----------|-------------|
| `!status` | Checks and displays the current Minecraft server status. |

---

## 🏛️ MySQL Database Setup
Run the following SQL command to create the required table:

```sql
CREATE TABLE server_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tps FLOAT,
    players INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🤝 Contributing
Pull requests are welcome! If you want to make significant changes, please open an issue first to discuss.

---
