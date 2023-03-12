import os
import threading

from fastapi import FastAPI

# pylint: disable=import-error
import src.temas_messenger as ms_messenger
import src.slack_messenger as slack_messenger
import src.schemas as schemas

app = FastAPI()

env = os.environ["ENV"]


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
