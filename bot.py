# ==================== 変な一言リスト（ここはそのまま） ====================
hitokoto_list = [
    "今日も頑張った自分を褒めたい",
    "お腹すいた…何かおいしいものないかな",
    "眠いけどまだ寝られない",
    "外の天気いいね、散歩したくなる",
    "仕事（学校）終わったらすぐ家に帰りたい",
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
    "愛知の今日の天気どうかな",
    "トヨタ周辺って信号多いよね",
    "夜更かししちゃった…後悔",
    # ここに自分で追加してもOK！
]

hitokoto = random.choice(hitokoto_list)

# ==================== ここを変更！ ====================
**final_post = hitokoto + " #bot"**   # ← 最後に #bot を付ける

print("選ばれた一言:", hitokoto)
print("最終投稿内容:", final_post)

# ==================== Karotter投稿部分 ====================
url = "https://karotter.com/api/developer/posts"

headers = {
    "x-api-key": os.getenv("KAROTTER_API_KEY"),
    "Content-Type": "application/json"
}

data = {
    "content": final_post   # ← ここも final_post に変更
}

print("送信URL:", url)
print("使用ヘッダー:", headers)   # キー自体は隠れるけど構造はわかる

response = requests.post(url, headers=headers, json=data)

print("ステータスコード:", response.status_code)
print("レスポンス本文:", response.text)

if response.status_code in [200, 201]:
    print("✅ 投稿成功！ → " + hitokoto)
else:
    print("❌ 失敗…")
