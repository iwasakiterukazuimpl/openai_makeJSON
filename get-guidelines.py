import base64
from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# 画像をbase64に変換
with open("guideline.png", "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode("utf-8")

prompt = """
以下のデザインガイドライン画像を解析し、
フォントや色のルールを JSON 形式にまとめてください。
必要に応じて H1/H2/body などの役割も推定してください。
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",  # 画像入力対応モデル
    messages=[
        {"role": "system", "content": "あなたはUIデザインのアシスタントです。"},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}}
            ]
        }
    ]
)

print(response.choices[0].message.content)