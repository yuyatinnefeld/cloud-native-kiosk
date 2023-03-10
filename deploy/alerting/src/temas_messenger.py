import pymsteams
import re


import src.schemas as schemas
from src.utils import get_webhook


def teams_notification(message: schemas.Message, project, env, provider) -> bool:
    webhook_url = get_webhook(env, provider)
    teams_message = pymsteams.connectorcard(webhook_url)
    teams_message.title(message.title)
    teams_message.text(message.text)

    if message.link is not None:
        teams_message.addLinkButton("Log Link", message.link)

    if message.color is not None:
        valid_hexcode = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", message.color)
        if valid_hexcode:
            teams_message.color(message.color)

    try:
        teams_message.send()
        status_code = teams_message.last_http_response.status_code
        print("ms teams status: ", status_code)
        return True

    except Exception as exc:
        print(f"error to send message to ms teams, exception: {exc}")
        return False
