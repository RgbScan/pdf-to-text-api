import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_extract_pdf():
    file_path = os.path.join(os.path.dirname(__file__), "CB_RF.pdf")
    with open(file_path, "rb") as f:
        response = client.post("/extract", files={"file": ("CB_RF.pdf", f, "application/pdf")})
    assert response.status_code == 200
    assert "text" in response.json()
    assert len(response.json()["text"]) > 0
