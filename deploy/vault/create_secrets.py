import hvac
import os


if __name__ == "__main__":
    VAULT_TOKEN = os.environ.get("VAULT_TOKEN")
    PWD_ALERTING_1 = os.environ.get("PWD_ALERTING_1")
    PWD_ALERTING_2 = os.environ.get("PWD_ALERTING_2")
    PWD_FRONTEND = os.environ.get("PWD_FRONTEND")
    PWD_BACKEND = os.environ.get("PWD_BACKEND")

    secret_list = [
        {"secret_path": "alerting/test_secret_1", "password": PWD_ALERTING_1},
        {"secret_path": "alerting/test_secret_2", "password": PWD_ALERTING_2},
        {"secret_path": "frontend/test_secret_1", "password": PWD_FRONTEND},
        {"secret_path": "backend/test_secret_1", "password": PWD_BACKEND},
    ]

    client = hvac.Client(
        url="http://127.0.0.1:8200",
        token=VAULT_TOKEN,
    )

    for item in secret_list:
        create_response = client.secrets.kv.v2.create_or_update_secret(
            path=item.get("secret_path"),
            secret=dict(password=item.get("password")),
        )
