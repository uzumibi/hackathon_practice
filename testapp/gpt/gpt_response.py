import base64
import json

import boto3
from botocore.exceptions import ClientError
from gpt.propmts import system_prompt, user_prompt


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_gpt(frame):
    session = boto3.Session(profile_name="test")
    client = session.client(service_name="bedrock-runtime", region_name="us-east-1")
    # image_path = "sample.jpeg"
    # base64_image = encode_image(image_path)
    base64_image = base64.b64encode(frame).decode("utf-8")
    modelID = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    body = json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 10,
            "temperature": 0.0,
            "system": system_prompt,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user_prompt,
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": f"{base64_image}",
                            },
                        },
                    ],
                }
            ],
        }
    )

    try:
        response = client.invoke_model(modelId=modelID, body=body)
    except (ClientError, Exception) as e:
        print(f"Error: {e}")
        exit(1)

    response_body = json.loads(response.get("body").read())
    response_text = response_body["content"][0]["text"]
    print(response_text)


if __name__ == "__main__":
    get_gpt()
