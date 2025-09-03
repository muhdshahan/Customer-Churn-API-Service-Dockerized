from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_app():
    data = {
  "Age": 56,
  "Gender": "Male",
  "Balance": 212801.73,
  "EstimatedSalary": 30322.86,
  "NumOfProducts": 1,
  "CreditScore": 847,
  "IsActiveMember": 0
}
    
    response = client.post('/predict', json=data)

    assert response.status_code==200

    json_data = response.json()

    assert 'prediction' in json_data
    assert 0 <= json_data['prediction'] <= 1