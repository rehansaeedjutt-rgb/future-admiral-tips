import os
import json
import random
import requests
from datetime import datetime
import pytz

WEBHOOK_URL = os.environ.get('DISCORD_WEBHOOK_URL')

def load_tips():
    """JSON file se saare tips load karta hai."""
    try:
        with open('data/tips.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Error loading tips: {e}")
        return {}

def get_random_tip(tips_data):
    """Har category se ek random tip uthata hai aur usay return karta hai."""
    all_tips = []
    
    # Saari categories ke tips ko ek list mein daalein
    for category, tips in tips_data.items():
        for tip in tips:
            all_tips.append(tip)
    
    if not all_tips:
        return None
    
    return random.choice(all_tips)

def send_to_discord(tip):
    """Tip ko Discord channel mein professional embed ke sath bhejta hai."""
    
    # Difficulty ke hisaab se emoji
    difficulty_emoji = {
        "Beginner": "🟢",
        "Intermediate": "🟡",
        "Advanced": "🔴"
    }
    
    # Category ke hisaab se emoji
    category_emoji = {
        "Technical Analysis": "📊",
        "Fundamental Analysis": "🌍",
        "Risk Management": "🛡️",
        "Trading Psychology": "🧠",
        "Market Wisdom": "💎"
    }
    
    diff_emoji = difficulty_emoji.get(tip.get("difficulty", "Beginner"), "🟢")
    cat_emoji = category_emoji.get(tip.get("category", "Market Wisdom"), "💎")
    
    embed = {
        "title": f"{cat_emoji} Tip of the Day — {tip.get('category', 'Trading')}",
        "description": f"\n**{tip.get('tip', '')}**\n",
        "color": 0x00d4ff,  # Cyan blue
        "fields": [
            {
                "name": "📚 Category",
                "value": tip.get("category", "N/A"),
                "inline": True
            },
            {
                "name": f"{diff_emoji} Level",
                "value": tip.get("difficulty", "Beginner"),
                "inline": True
            }
        ],
        "footer": {
            "text": "Future Admiral | Education • Daily Tips",
            "icon_url": "https://cdn-icons-png.flaticon.com/512/2917/2917995.png"
        },
        "timestamp": datetime.now(pytz.utc).isoformat()
    }
    
    payload = {
        "embeds": [embed],
        "username": "Future Admiral — Education"
    }
    
    response = requests.post(WEBHOOK_URL, json=payload)
    
    if response.status_code == 204:
        print(f"✅ Tip successfully bhej diya: {tip.get('tip', '')[:50]}...")
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    print("📚 Daily tip fetch kar rahe hain...")
    tips_data = load_tips()
    
    if not tips_data:
        print("❌ Tips data load nahi ho saka.")
    else:
        tip = get_random_tip(tips_data)
        if tip:
            send_to_discord(tip)
        else:
            print("❌ Koi tip available nahi hai.")
