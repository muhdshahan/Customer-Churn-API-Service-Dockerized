from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_app():
    data = {"features": [1,56,"Male",212801.73,30322.86,1,847,0]}
    response = client.post('/predict', json=data)

    assert response.status_code==200

    json_data = response.json()

    assert 'prediction' in json_data
    assert 0 <= json_data['prediction'] <= 1