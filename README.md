
# Telepump / TON Mini Bot — Render-ready

This project is a minimal, Render-ready skeleton for a Telegram bot that will later integrate with TON (Jettons) and DEX auto-listing. It's designed to run as a **Background Worker** on Render (free tier) and uses `pydantic-settings` to be compatible with Pydantic v2.

## Quickstart (local)

1. Create venv and activate:
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy .env.example to .env and add your BOT_TOKEN:
```
BOT_TOKEN=123456:ABC...yourtoken
```

4. Run locally:
```bash
python main.py
```

## Deploy on Render (Background Worker)

- Build command:
```
pip install -r requirements.txt
```
- Start command:
```
python main.py
```
- Add Environment Variable on Render: `BOT_TOKEN`

Tip: choose the **Background Worker** service type. The free plan provides limited monthly hours — good for testing. For production 24/7, upgrade the plan.

## Next steps to implement real features
- Replace `app/services/ton.py` with tonsdk implementation to deploy Jettons on testnet/mainnet.
- Implement `app/services/dex.py` to call DEX APIs (STON.fi / DeDust) for pool creation and liquidity.
- Add persistent DB (SQLite/Postgres) for referrals and game state.
