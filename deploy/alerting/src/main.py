import os
import threading

from fastapi import FastAPI

# pylint: disable=import-error
import src.temas_messenger as ms_messenger
import src.slack_messenger as slack_messenger
import src.schemas as schemas

import utils

app = FastAPI()

env = os.environ["ENV"]
vault_token = os.environ["VAULT_TOKEN"]


if env == "LOCAL_FOR_VAULT":
    secret_path = "alerting/test_secret_1"
    pwd = utils.access_vault_password(vault_token, "http://127.0.0.1:8200", secret_path)
    print(pwd)


@app.post("/teams", response_model=schemas.Message)
async def teams_chat(message: schemas.Message):
    threading.Thread(
        target=ms_messenger.teams_notification, args=(message, env, "TEAMS")
    ).start()
    return message


@app.post("/slack")
async def slack_chat(message: schemas.Message):
    threading.Thread(
        target=slack_messenger.slack_notification,
        args=(message, env, "SLACK"),
    ).start()
    return message
