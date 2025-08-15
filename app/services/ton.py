
# Placeholder TON utilities.
# When ready for real deployment, replace demo functions with actual SDK calls (tonsdk/tonlib).
def create_ton_token_demo(name: str, symbol: str) -> dict:
    return {
        "name": name,
        "symbol": symbol,
        "address": "0:demoaddress1234567890abcdef",
        "explorer": "https://tonscan.org/address/0:demoaddress1234567890abcdef"
    }
