import os
import threading

from fastapi import FastAPI

# pylint: disable=import-error
import src.temas_messenger as ms_messenger
import src.slack_messenger as slack_messenger
import src.schemas as schemas

app = FastAPI()

env = os.environ["ENV"]
project = os.environ["GCP_PROJECT_ID"]


@app.post("/teams", response_model=schemas.Message)
async def teams_chat(message: schemas.Message):
    provider = "TEAMS"
    threading.Thread(
        target=ms_messenger.teams_notification, args=(message, project, env, provider)
    ).start()
    return message


@app.post("/slack")
async def slack_chat(message: schemas.Message):
    provider = "SLACK"
    threading.Thread(
        target=slack_messenger.slack_notification,
        args=(message, project, env, provider),
    ).start()
    return message
