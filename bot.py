import json
import os
import urllib.request

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
SLOT = os.environ.get("SLOT", "morning")  # morning / noon / evening


def build_message(slot: str) -> str:
    message = (
        "夜の秘密ラウンジへようこそ🌙\n"
        "ここは\n"
        "大人の女の子たちが集まる\n"
        "秘密のナイトラウンジです。\n\n"
        "💋 新しい出会い\n"
        "💋 夜の楽しい会話\n"
        "💋 魅力的な女の子たち\n"
        "そんな夜の時間を一緒に楽しみませんか？\n\n"
        "✨ 女の子メンバー募集中\n"
        "✨ 気軽に参加OK\n"
        "👇参加はこちら\n"
        "telegram\n"
        "https://t.me/+CoNGESydKIwyYjI0\n"
        "シグナル\n"
        "https://signal.group/#CjQKIPdSY2w4wY87HxZY-qdJ0WNLWHcqjxWCRv0FEc9ViQ5VEhCn3kyfaS6cGaRTLj45q4HW\n"
    )
    return message


def send_telegram_message(token: str, chat_id: str, text: str) -> dict:
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": False,
    }

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=30) as response:
        body = response.read().decode("utf-8")
        return json.loads(body)


def main():
    message = build_message(SLOT)
    result = send_telegram_message(BOT_TOKEN, CHAT_ID, message)

    if not result.get("ok"):
        raise RuntimeError(f"Telegram API error: {result}")

    print(f"Posted successfully: {SLOT}")


if __name__ == "__main__":
    main()