import random
import os
import requests

# ここに変な一言をたくさん書いてね（30個以上おすすめ）
hitokoto_list = [
    "おはよう",
    "こんにちは",
    "暇だ",
    "晴れてる？",
    "雨降ってる？",
    "曇ってる？",
    "雷鳴ってる？",
    "引っ越したい",
    "眠いな",
    "疲れた...",
  　
    # ← ここにどんどん追加して！
]

# ランダムに1つ選ぶ
hitokoto = random.choice(hitokoto_list)

# Karotterに投稿
url = "https://karotter.com/api/developer/posts"  # 投稿エンドポイント（公式ドキュメントで確認してね）
headers = {
    "Authorization": f"Bearer {os.getenv('KAROTTER_API_KEY')}",
    "Content-Type": "application/json"
}
data = {
    "content": hitokoto,
    # 必要なら "visibility": "public" なども追加
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201 or response.status_code == 200:
    print("✅ 投稿成功！ → " + hitokoto)
else:
    print("❌ 失敗…", response.status_code, response.text)
