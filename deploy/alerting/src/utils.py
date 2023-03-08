import os

from google.cloud import secretmanager


def get_webhook(
    message_title="Default Title",
    project: str = "ProjectID",
    env: str = "LOCAL",
    provider: str = "",
):
    if provider == "SLACK":
        return os.environ["SLACK_WEBHOOK"] if env == "LOCAL" else "No"

    elif provider == "TEAMS":
        return os.environ["TEAMS_WEBHOOK"] if env == "LOCAL" else "No"

        if "CNK ERROR" in message_title:
            secret_name = "teams_webhook_error"
        elif "CNK SUCCESS" in message_title:
            secret_name = "teams_webhook_success"
        else:
            raise Exception("check the message.title !")

        client = secretmanager.SecretManagerServiceClient()
        response = client.access_secret_version(
            request={
                "name": f"projects/{project}/secrets/{secret_name}/versions/latest"
            }
        )

        return response.payload.data.decode("UTF-8")

    else:
        print("check the provider environement variable")
