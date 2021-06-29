def test_index(app, client):
    result = client.get('/')
    assert result.status_code == 200