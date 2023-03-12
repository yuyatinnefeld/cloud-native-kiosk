from httpx import AsyncClient
import pytest

from src import main


@pytest.mark.asyncio
async def test_teams_notification():
    async with AsyncClient(app=main.app, base_url="http://test") as ac:
        response = await ac.post("/teams", json={})
        print("TEAMS RESPONSE: ", response)

    assert response.status_code == 200

    test_json = {
        "title": "UNIT TEST - TEAMS",
        "text": "This is a test message to check the microsoft teams alerting function.",
        "color": "#5F9EA0",
    }

    async with AsyncClient(app=main.app, base_url="http://test") as ac:
        response = await ac.post("/teams", json=test_json)

    test_json.update({"link": "https://example.com"})
    test_json.update({"color": "#5F9EA0"})

    assert test_json == response.json()
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_slack_notification():
    async with AsyncClient(app=main.app, base_url="http://test") as ac:
        response = await ac.post("/slack", json={})
        print("SLACK RESPONSE: ", response)

    assert response.status_code == 200

    test_json = {
        "title": "UNIT TEST - SLACK",
        "text": "This is a test message to check the slack alerting function.",
        "color": "#5F9EA0",
    }

    async with AsyncClient(app=main.app, base_url="http://test") as ac:
        response = await ac.post("/slack", json=test_json)

    test_json.update({"link": "https://example.com"})
    test_json.update({"color": "#5F9EA0"})

    assert test_json == response.json()
    assert response.status_code == 200
