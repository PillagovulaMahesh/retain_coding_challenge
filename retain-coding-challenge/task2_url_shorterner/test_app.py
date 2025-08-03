import pytest
from app import app, store

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_shorten_url(client):
    response = client.post("/api/shorten", json={"url": "https://example.com"})
    assert response.status_code == 200
    data = response.get_json()
    assert "short_code" in data
    assert "short_url" in data

def test_invalid_url(client):
    response = client.post("/api/shorten", json={"url": "not-a-url"})
    assert response.status_code == 400

def test_redirect(client):
    response = client.post("/api/shorten", json={"url": "https://example.com"})
    short_code = response.get_json()["short_code"]
    redirect_response = client.get(f"/{short_code}", follow_redirects=False)
    assert redirect_response.status_code == 302

def test_stats(client):
    response = client.post("/api/shorten", json={"url": "https://example.com"})
    short_code = response.get_json()["short_code"]
    stats_response = client.get(f"/api/stats/{short_code}")
    assert stats_response.status_code == 200
    stats_data = stats_response.get_json()
    assert stats_data["clicks"] >= 0
    assert "created_at" in stats_data

def test_invalid_code_redirect(client):
    response = client.get("/nonexist", follow_redirects=False)
    assert response.status_code == 404
