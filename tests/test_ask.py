import json
def test_ask(client):
    response = client.post("/ask",json={
  "question": "how much is 9+10?"
})
      
    assert json.loads(response.data.decode())['answer'] =="9 + 10 = 19"
