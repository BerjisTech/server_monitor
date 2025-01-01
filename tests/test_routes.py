import pytest
from app import create_app
from app.extensions import db
from app.models import Server

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to the Server Monitor API!"}

def test_add_server(client):
    server_data = {"name": "Test Server", "ip_address": "192.168.1.1"}
    response = client.post("/servers", json=server_data)
    assert response.status_code == 201
    assert response.json["name"] == "Test Server"
