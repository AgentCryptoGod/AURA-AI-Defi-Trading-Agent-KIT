from setuptools import setup, find_packages

setup(
    name="agent_sniper_solana",
    version="1.0.0",
    author="Aura Labs",
    description="AI-powered Sniper Trading Agent for Solana using GPT-4 and Solana Agent Kit.",
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
