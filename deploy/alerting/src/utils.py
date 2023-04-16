import hvac
import os


def access_vault_password(vault_token: str, vault_url: str, secret_path: str):
    client = hvac.Client(
        url=vault_url,
        token=vault_token,
    )
    read_response = client.secrets.kv.read_secret_version(path=secret_path)
    password = read_response["data"]["data"]["password"]
    return password


def get_webhook(env: str = "LOCAL", provider: str = None):
    if provider == "SLACK":
        return (
            os.environ["SLACK_WEBHOOK"]
            if env == "LOCAL" or env == "CICD"
            # from GCP Service manageer
            else os.environ["webhook_url_slack_error"]
        )

    elif provider == "TEAMS":
        return (
            os.environ["TEAMS_WEBHOOK"]
            if env == "LOCAL" or env == "CICD"
            # from GCP Service manageer
            else os.environ["webhook_url_teams_error"]
        )

    else:
        raise Exception("check the provider!")
