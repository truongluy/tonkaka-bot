
# TON Mini Bot

Bot Telegram cho TON blockchain — hỗ trợ tạo token nhanh, auto list DEX, mini game và affiliate.

## Cấu trúc dự án
- `bot/commands/` — các lệnh bot (`/create`, `/game`, `/referral`, ...)
- `ton/` — xử lý blockchain TON (tạo token, kết nối DEX)
- `db/` — lưu dữ liệu user, token, game, referral
- `config.py` — đọc biến môi trường
- `main.py` — entry point

## Chạy thử
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Sửa BOT_TOKEN trong .env
python main.py
```

Sau khi chạy, gõ /start hoặc /help trong Telegram để kiểm tra bot.
