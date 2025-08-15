
# Placeholder cho xử lý blockchain TON.
# Khi triển khai thật, thay thế hàm demo bằng gọi SDK (tonsdk/tonpy).
def create_ton_token_demo(name: str, symbol: str):
    # Trả về dữ liệu giả lập để test bot
    return {
        "name": name,
        "symbol": symbol,
        "address": "0:demoaddress1234567890abcdef",
        "explorer": "https://tonviewer.com/0:demoaddress1234567890abcdef"
    }
