'''
# CREATE USER pytest_user WITH PASSWORD 'pystest_user_password';
# CREATE DATABASE pytest_test;
# GRANT ALL PRIVILEGES ON DATABASE pytest_test TO pytest_user;
app = FastAPI()

DATABASE_URL = "postgresql://pytest_user:pystest_user_password@localhost:5432/pytest_test"
'''




from fastapi.testclient import TestClient


def test_create_item(main_app):
    item_data = {"name": "Test Item", "description": "Test description"}
    client = TestClient(main_app)
    response = client.post("/item", json=item_data)
    print(response.json())
    assert response.status_code == 200
def test_read_items3(main_app):
    client = TestClient(main_app)
    response = client.get("/items")
    assert response.status_code == 200

# Test case for reading an item
# def test_read_item(client):
#     item_data = {"name": "Test Item", "description": "Test description"}
#     response = client.post("/item", json=item_data)
#     item_id = response.json()["id"]
#     response = client.get(f"/items/{item_id}")
#     assert response.status_code == 200
#     assert response.json()["id"] == item_id
#     assert response.json()["name"] == item_data["name"]

# Test case for reading an item's name
# def test_read_item_name(client):
#     item_data = {"name": "Test Item", "description": "Test description"}
#     response = client.post("/item", json=item_data)
#     item_id = response.json()["id"]
#     response = client.get(f"/items/{item_id}/name")
#     assert response.status_code == 200
#     assert response.json()["id"] == item_id
#     assert response.json()["name"] == item_data["name"]

# Test case for reading all items
# def test_read_items(client):

#     response = client.get("/items")
#     assert response.status_code == 200
# def test_read_items7(client):

#     response = client.get("/items")
#     assert response.status_code == 200


# def test_read_items1(client):

#     response = client.get("/items")
#     assert response.status_code == 200

# def test_read_items2(client):

#     response = client.get("/items")
#     assert response.status_code == 200


