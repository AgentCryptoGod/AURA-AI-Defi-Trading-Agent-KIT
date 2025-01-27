import numpy as np
import random
from solana_agent_kit import SolanaAgentKit, createSolanaTools, executeAction
from openai import OpenAI
from telegram import Bot
import asyncio

class AISniperAgent:
    def __init__(self, solana_private_key, openai_api_key, telegram_bot_token):
        self.agent = SolanaAgentKit(private_key=solana_private_key, rpc_url="https://api.mainnet-beta.solana.com", openai_api_key=openai_api_key)
        self.tools = createSolanaTools(self.agent)
        self.openai_client = OpenAI(api_key=openai_api_key)
        self.telegram_bot = Bot(token=telegram_bot_token)

    async def send_telegram_message(self, chat_id, message):
        await self.telegram_bot.send_message(chat_id=chat_id, text=message)

    def snipe_new_token(self, pair_address, amount):
        decision = self.openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Analyze if the new token is a good investment."},
                      {"role": "user", "content": f"Should I snipe {amount} SOL into {pair_address}?"}]
        )
        if "yes" in decision.choices[0].message.content.lower():
            response = executeAction(self.agent, "jupiter_exchange_swaps", {
                "inputToken": "SOL",
                "outputToken": pair_address,
                "amount": amount
            })
            asyncio.run(self.send_telegram_message("your-chat-id", f"Sniped {amount} SOL into {pair_address}"))
            return response
        return "Sniper decision: No action taken"

    def snipe_nft(self, nft_address):
        decision = self.openai_client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Analyze if the NFT is undervalued and worth sniping."},
                      {"role": "user", "content": f"Should I snipe NFT from {nft_address}?"}]
        )
        if "yes" in decision.choices[0].message.content.lower():
            response = executeAction(self.agent, "mint_nft", {"collection": nft_address})
            asyncio.run(self.send_telegram_message("your-chat-id", f"NFT Sniped: {nft_address}"))
            return response
        return "NFT Sniper decision: No action taken"
