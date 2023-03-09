# Alerting Service

open the working directory
```bash
cd deploy/alerting
```

## Local Application Debug

```bash
export GCP_PROJECT_ID=<YOUR GCP PROJECT ID>
export ENV=LOCAL
export PROVIDER=TEAMS
export SLACK_WEBHOOK="https://hooks.slack.com/services/????/???/???"
export TEAMS_WEBHOOK="https://???.webhook.office.com/webhookb2/????/IncomingWebhook/????/????"

pip install -r requirements.txt
uvicorn src.main:app --reload
```

## Build & Run Docker image
```bash
docker build -t alerting-image .
docker run -it -p 8080:8080 alerting-image

# verify
open http://127.0.0.1:8080/docs
```

## Local Deployment
```bash
SERVICE_NAME="cnk-alerting"
GCP_IMAGE_NAME="eu.gcr.io/${PROJECT_ID}/cnk-alerting:1.0.0"
CLOUD_RUN_ID="<your-cloud-run-id>"

# push the image
gcloud builds submit --substitutions _IMAGE=${GCP_IMAGE_NAME}

# deploy cloud run
gcloud run deploy ${SERVICE_NAME} \
    --image ${GCP_IMAGE_NAME} \
    --platform managed \
    --region=europe-west1 \
    --memory=512Mi \
    --min-instances=1 \
    --max-instances=2 \
    --no-allow-unauthenticated \
    --update-env-vars=GCP_PROJECT_ID=$PROJECT_ID,ENV=DEV

open https://${SERVICE_NAME}-${CLOUD_RUN_ID}-ew.a.run.app/docs
```
