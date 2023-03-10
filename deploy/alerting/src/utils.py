import os


def get_webhook(env: str = "LOCAL", provider: str = None):
    if provider == "SLACK":
        return (
            os.environ["SLACK_WEBHOOK"]
            if env == "LOCAL"
            # from GCP Service manageer
            else os.environ["webhook_url_slack_error"]
        )

    elif provider == "TEAMS":
        return (
            os.environ["TEAMS_WEBHOOK"]
            if env == "LOCAL"
            # from GCP Service manageer
            else os.environ["webhook_url_teams_error"]
        )

    else:
        raise Exception("check the provider!")
