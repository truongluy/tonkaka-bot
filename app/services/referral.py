
def generate_ref_link(user_id: int) -> str:
    # Telegram deep-link format (replace 'your_bot_username' before production)
    return f'https://t.me/your_bot_username?start=ref{user_id}'
