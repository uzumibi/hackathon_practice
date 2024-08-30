# cotomiに画像投げるのは俺には無理だった
import base64

from openai import OpenAI

from basics.prompts import system_prompt, user_prompt

image_path = "basics/sample.jpg"


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def gpt():
    client = OpenAI(
        api_key="a72bd044bae740a4a66d8372a111a09d",
        base_url="https://api.cotomi.nec-cloud.com/oai-api/v1",
    )
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model="cotomi-core-pro-v1.0-awq",  # モデルの名前
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            },
        ],  # 入力するプロンプト
        temperature=0.7,  # 出力のランダム度合い(可変)
        max_tokens=800,  # 最大トークン数(固定)
        top_p=0.95,  # 予測する単語を上位何%からサンプリングするか(可変)
        frequency_penalty=0,  # 単語の繰り返しをどのくらい許容するか(可変)
        presence_penalty=0,  # 同じ単語をどのくらい使うか(可変)
        stop=None,  # 文章生成を停止する単語を指定する(可変)
    )

    # GPTの出力を表示
    print(response.choices[0].message.content.strip())


if __name__ == "__main__":
    gpt()
