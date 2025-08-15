
# TON Mini Bot (Render-ready)

Bot Telegram mẫu cho hệ sinh thái TON — tách module rõ ràng, tối ưu deploy Background Worker trên Render.

## Chạy local
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # điền BOT_TOKEN
python main.py
```

## Deploy Render (Background Worker)
- **Build command**:
```
pip install -r requirements.txt
```
- **Start command**:
```
python main.py
```
- **Env vars**: thêm `BOT_TOKEN` trong Dashboard Render.

## Mở rộng
- Triển khai thật TON: thay `app/services/ton_utils.py` bằng gọi SDK (tonsdk/tonpy)
- Auto-list DEX: viết trong `app/services/dex_utils.py`
- Referral nâng cao + DB: thêm module DB (SQLite/Postgres) và lưu ref/link/point.
