
def generate_ref_link(user_id: int) -> str:
    # Sử dụng deep-link Telegram chuẩn
    return f"https://t.me/your_bot_username?start=ref{user_id}"
