from fastapi.testclient import TestClient
from app.main import app
c=TestClient(app)
def test_sync_boundary():
    b={"device_id":"d1","kind":"contacts"}
    assert c.post("/v1/sync/jobs",json=b).status_code==401
    assert c.post("/v1/sync/jobs",headers={"x-service-identity":"control-server"},json=b).status_code==202
