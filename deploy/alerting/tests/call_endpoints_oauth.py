import json
import os

import google.auth.transport.requests
import google.oauth2.id_token
import urllib


def call_http_cloud_run(service_url_full, data) -> str:
    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, service_url_full)
    req = urllib.request.Request(service_url_full, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {id_token}")

    json_data = json.dumps(data).encode("utf-8")
    response = urllib.request.urlopen(req, json_data)
    print(response)
    result = response.read().decode("utf-8")
    return result


cloud_run_id = os.environ["CLOUD_RUN_ID"]
service_url = f"https://cnk-alerting-${cloud_run_id}-ew.a.run.app/"
service_url_full = f"{service_url}/teams"

data = {
    "title": "CNK ERROR",
    "text": "this is a placeholder text from FastAPI alerting backend",
    "link": "https://example.com",
    "color": "#5F9EA0",
}


result = call_http_cloud_run(service_url_full, data)
print(result)
