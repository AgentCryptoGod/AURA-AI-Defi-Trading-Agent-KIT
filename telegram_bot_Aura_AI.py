from telegram import Bot

bot = Bot(token="your-telegram-bot-token")

def send_trade_alert(message):
    chat_id = "your-chat-id"
    bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    send_trade_alert("Test alert: AI trading bot is live!")
