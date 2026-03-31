"""Telegram bot for financial intelligence via VEROQ.

Handles /ask, /price, and /verify commands using python-telegram-bot.
Runs as a webhook handler behind any HTTPS endpoint (Railway, Vercel,
etc.) for production use, or long-polling for local development.
"""
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from veroq import VeroqClient

veroq = VeroqClient()

async def cmd_ask(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """Handle /ask <question> — full financial intelligence."""
    query = " ".join(ctx.args) if ctx.args else ""
    if not query:
        await update.message.reply_text("Usage: /ask What is AAPL's outlook?")
        return

    await update.message.reply_text("Researching...")
    result = veroq.ask(query)

    # Format a clean Telegram message with Markdown
    lines = [f"*{query}*", "", result["summary"][:3000]]
    signal = result.get("trade_signal", {})
    if signal:
        lines.append(f"\nSignal: *{signal['action'].upper()}* ({signal['score']}/100)")
    lines.append(f"Confidence: {result['confidence']['level']}")

    await update.message.reply_text("\n".join(lines), parse_mode="Markdown")

async def cmd_price(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """Handle /price <ticker> — quick price check."""
    ticker = ctx.args[0].upper() if ctx.args else ""
    if not ticker:
        await update.message.reply_text("Usage: /price NVDA")
        return

    result = veroq.ask(f"{ticker} current price and change")
    data = result.get("data", {}).get("ticker", {}).get("price", {})
    text = (
        f"*{ticker}*\n"
        f"Price: ${data.get('current', '?')}\n"
        f"Change: {data.get('change_pct', '?')}%\n"
        f"Volume: {data.get('volume', '?')}"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def cmd_verify(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    """Handle /verify <claim> — fact-check with sources."""
    claim = " ".join(ctx.args) if ctx.args else ""
    if not claim:
        await update.message.reply_text("Usage: /verify Tesla beat Q4 earnings")
        return

    result = veroq.verify(claim)
    verdict_map = {"true": "Confirmed", "false": "Disputed", "unverified": "Unclear"}
    text = f"*{verdict_map.get(result['verdict'], '?')}* ({result['confidence']*100:.0f}%)\n\n"
    for ev in result["evidence_chain"][:3]:
        text += f"- {ev['source']}: {ev['snippet'][:120]}\n"

    await update.message.reply_text(text, parse_mode="Markdown")

# Build and run the bot
app = Application.builder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
app.add_handler(CommandHandler("ask", cmd_ask))
app.add_handler(CommandHandler("price", cmd_price))
app.add_handler(CommandHandler("verify", cmd_verify))

# Local dev: long-polling. Production: set WEBHOOK_URL for webhook mode.
if os.environ.get("WEBHOOK_URL"):
    app.run_webhook(listen="0.0.0.0", port=8443, webhook_url=os.environ["WEBHOOK_URL"])
else:
    app.run_polling()
