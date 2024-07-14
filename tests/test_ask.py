def test_ask(client):
    response = client.post("/ask",json={
  "question": "Why is the sky blue?"
})
    print(response.data.decode())  
    assert response.status_code == 200
    # assert response.data.decode() == "pong!"
