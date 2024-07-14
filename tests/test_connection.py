def test_ping(client):
    response = client.get("/ping")
    print(response.data.decode())  
    assert response.status_code == 200
    assert response.data.decode() == "pong!"

