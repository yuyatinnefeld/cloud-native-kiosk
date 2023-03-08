import json
import urllib3

import src.schemas as schemas

from src.utils import get_webhook


def slack_notification(message: schemas.Message, project, env, provider) -> bool:
    webhook_url = get_webhook(message.title, project, env, provider)
    http = urllib3.PoolManager()

    attachments = [
        {
            "title": message.title,
            "text": message.text,
        }
    ]

    if message.link is not None:
        attachments[0]["title_link"] = message.link

    if message.color is not None:
        attachments[0]["color"] = message.color

    slack_message = {"attachments": attachments}

    try:
        response = http.request(
            "POST",
            webhook_url,
            body=json.dumps(slack_message),
            headers={"Content-Type": "application/json"},
            retries=False,
        )
        print("status: ", response.status)
        return True

    except Exception as exc:
        print(f"error to send message to ms teams, exception: {exc}")
        return False
