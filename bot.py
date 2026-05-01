import random
import os
import requests

# ==================== 日常の一言リスト ====================
hitokoto_list = [
    "今日も頑張った自分を褒めたい",
    "お腹すいた…何かおいしいものないかな",
    "眠いけどまだ寝られない",
    "外の天気いいね、散歩したくなる",
    "学校（仕事）終わったらすぐ家に帰りたい",
    "なんか甘いもの食べたい気分",
    "最近疲れが溜まってる気がする",
    "友達に連絡しようかな…",
    "今日の夕飯何にしよう",
    "雨降ってきた…傘持ってきてよかった",
    "朝のコーヒーが一番好き",
    "なんかいいことないかな〜",
    "ベッドが恋しい",
    "音楽聞きながらぼーっとしたい",
    "明日も頑張ろう",
    "今めっちゃ集中してる",
    "ちょっと休憩したい",
    "夜更かししちゃった…後悔",
    "今日も一日お疲れ様",
    "なんか癒されたい",
    "明日はいい日になりますように",
    "ちょっとだけ頑張る",
    "家に帰ってゆっくりしたい",
    "眠すぎる...今夜は早く寝よう"
]

# ランダムに1つ選ぶ
hitokoto = random.choice(hitokoto_list)

# 最後に #bot を付ける
final_post = hitokoto + " #bot"

print("選ばれた一言:", hitokoto)
print("最終投稿内容:", final_post)

# ==================== Karotterに投稿 ====================
url = "https://karotter.com/api/developer/posts"

headers = {
    "x-api-key": os.getenv("KAROTTER_API_KEY"),
    "Content-Type": "application/json"
}

data = {
    "content": final_post
}

response = requests.post(url, headers=headers, json=data)

print("ステータスコード:", response.status_code)
print("レスポンス:", response.text)

if response.status_code in [200, 201]:
    print("✅ 投稿成功！ → " + final_post)
else:
    print("❌ 投稿失敗…")
