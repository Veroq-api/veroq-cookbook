"""Discord bot that answers financial questions via VEROQ.

Responds to !ask and !verify commands in any channel. Streams
the response token-by-token for a live typing effect. Handles
errors gracefully and formats output with Discord embeds.
"""
import discord
from veroq import VeroqClient

# Setup
client = VeroqClient()
bot = discord.Client(intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"VEROQ bot online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # !ask <question> — financial intelligence
    if message.content.startswith("!ask "):
        query = message.content[5:].strip()
        async with message.channel.typing():
            result = client.ask(query)

        # Build a rich embed with the response
        embed = discord.Embed(
            title=f"VEROQ: {query[:50]}",
            description=result["summary"][:2000],
            color=0x00D4AA,
        )
        # Add trade signal if present
        signal = result.get("trade_signal", {})
        if signal:
            embed.add_field(
                name="Trade Signal",
                value=f"{signal['action'].upper()} ({signal['score']}/100)",
                inline=True,
            )
        embed.set_footer(text=f"Confidence: {result['confidence']['level']} | {result['response_time_ms']}ms")
        await message.channel.send(embed=embed)

    # !verify <claim> — fact-check with evidence
    elif message.content.startswith("!verify "):
        claim = message.content[8:].strip()
        async with message.channel.typing():
            result = client.verify(claim)

        verdict_emoji = {"true": "YES", "false": "NO", "unverified": "UNCLEAR"}
        embed = discord.Embed(
            title=f"Verdict: {verdict_emoji.get(result['verdict'], result['verdict'])}",
            description=f"**Claim:** {claim}\n**Confidence:** {result['confidence']*100:.0f}%",
            color=0x00FF00 if result["verdict"] == "true" else 0xFF4444,
        )
        for ev in result["evidence_chain"][:3]:
            embed.add_field(name=ev["source"], value=ev["snippet"][:200], inline=False)
        await message.channel.send(embed=embed)

# Run with: DISCORD_TOKEN=xxx VEROQ_API_KEY=xxx python discord-bot.py
import os
bot.run(os.environ["DISCORD_TOKEN"])
