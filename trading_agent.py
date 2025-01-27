import numpy as np
import random
from solana_agent_kit import SolanaAgentKit, createSolanaTools, executeAction
from openai import OpenAI
from telegram import Bot
from fastapi import FastAPI
import asyncio

class AITradingAgent:
    def __init__(self, solana_private_key, openai_api_key, telegram_bot_token):
        self.agent = SolanaAgentKit(private_key=solana_private_key, rpc_url="https://api.mainnet-beta.solana.com", openai_api_key=openai_api_key)
        self.tools = createSolanaTools(self.agent)
        self.openai_client = OpenAI(api_key=openai_api_key)
        self.telegram_bot = Bot(token=telegram_bot_token)
        self.app = FastAPI()

    async def send_telegram_message(self, chat_id, message):
        await self.telegram_bot.send_message(chat_id=chat_id, text=message)

    def swap_tokens(self, input_token, output_token, amount):
        decision = self.openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Decide whether to swap based on market conditions."},
                      {"role": "user", "content": f"Should I swap {amount} {input_token} for {output_token}?"}]
        )
        if "yes" in decision.choices[0].message.content.lower():
            response = executeAction(self.agent, "jupiter_exchange_swaps", {"inputToken": input_token, "outputToken": output_token, "amount": amount})
            asyncio.run(self.send_telegram_message("your-chat-id", f"Swap Executed: {amount} {input_token} for {output_token}"))
            return response
        return "Swap decision: No action taken"
