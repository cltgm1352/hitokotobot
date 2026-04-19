import random
import os
import requests

# ==================== 変な一言リスト（ここを充実させて！） ====================
hitokoto_list = [
    "今日も靴下が片方だけ宇宙旅行に行った🌀",
    "冷蔵庫のプリンが俺を睨んでる気がする",
    "朝起きたら枕が哲学を語り始めた",
    "カレーのルーだけが先に幸せになった",
    "今、雲が俺の名前を呼んだ気がする",
    "歯ブラシが突然上司になった",
    "考え中（考えてはいない）",
    "人生、仮置き状態です",
    "金曜日はいつもカタカナで来る",
    "ラッセンが俺の宿題を食った",
    "ポテトチップスの波長が合わない",
    "靴下だけ先に出勤した",
    "気分は概念です",
    "本気は家に忘れてきた",
    "Karotterで1文字ID取ろうとして人生取られた",
    "ストーリー機能で自分の顔が溶けた",
    "通話中に突然猫になった",
    # ここにまだ足りなければ追加して！
]

hitokoto = random.choice(hitokoto_list)

print("選ばれた一言:", hitokoto)

# ==================== Karotter投稿部分 ====================
url = "https://karotter.com/api/developer/posts"

# まずは x-api-key で試す（公式推奨）
headers = {
    "x-api-key": os.getenv("KAROTTER_API_KEY"),
    "Content-Type": "application/json"
}

data = {
    "content": hitokoto
    # 必要なら追加: "visibility": "public"
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
