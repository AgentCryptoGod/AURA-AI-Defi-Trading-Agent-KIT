from setuptools import setup, find_packages

setup(
    name="aura_ai_defi_toolkit",
    version="1.0.0",
    author="Aura Labs",
    description="AI-powered DeFi trading agent using Solana, GPT-4, and Swarm Intelligence.",
    packages=find_packages(),
    install_requires=[
        "solana-agent-kit",
        "openai",
        "fastapi",
        "uvicorn",
        "python-telegram-bot"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
