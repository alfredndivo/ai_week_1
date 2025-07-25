crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

print("👋 Hey there! I’m CryptoBuddy – your AI-powered crypto sidekick!")
print("Ask me about trending coins, sustainability, or long-term advice.")

while True:
    user_query = input("\nYou: ").lower()
    
    if "exit" in user_query or "quit" in user_query:
        print("CryptoBuddy: 🚪 Logging out! Remember, always DYOR (Do Your Own Research)!")
        break



    elif "sustainable" in user_query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: 🌱 Go with {best}! It's eco-friendly and scores {crypto_db[best]['sustainability_score']}/10 in sustainability.")

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"CryptoBuddy: 📈 These coins are trending up: {', '.join(trending)}")

    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                print(f"CryptoBuddy: 🚀 {coin} is great for long-term growth. Rising trend + High sustainability!")
                break

    elif "most popular" in user_query or "high market cap" in user_query:
        popular = [coin for coin in crypto_db if crypto_db[coin]["market_cap"] == "high"]
        print(f"CryptoBuddy: 💰 High market cap coins include: {', '.join(popular)}")

    else:
        print("CryptoBuddy: 🤖 Hmm, I’m not sure. Try asking about trends, sustainability, or market cap.")

print("\n⚠️ Crypto is risky—always do your own research before investing!")
