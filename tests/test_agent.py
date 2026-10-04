from fastapi.testclient import TestClient
from autocloud.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'operate the landing zone', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["steps"][1] == "decide"
    refused = client.post("/agent/run", json={"goal": 'destroy the project'}).json()
    assert refused["refused"] is True
