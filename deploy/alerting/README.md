# Alerting Service Local Debug

```bash
cd deploy/alerting
pip install -r requirements_dev.txt
export GCP_PROJECT_ID=yuyatinnefeld-dev
export ENV=LOCAL
export PROVIDER=TEAMS
export SLACK_WEBHOOK="https://hooks.slack.com/services/????/???/???"
export TEAMS_WEBHOOK="https://???.webhook.office.com/webhookb2/????/IncomingWebhook/????/????"
uvicorn src.main:app --reload
```
