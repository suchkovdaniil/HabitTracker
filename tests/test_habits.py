from datetime import date, timedelta

def test_create_habit(client):
    response = client.post("/habits/", json={
        "name": "Чтение",
        "description": "Читать каждый вечер"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Чтение"

def test_create_duplicate_habit(client):
    response = client.post("/habits/", json={
        "name": "Чтение",
        "description": "Повтор"
    })
    assert response.status_code == 400

def test_list_habits(client):
    response = client.get("/habits/")
    assert response.status_code == 200
    habits = response.json()
    assert isinstance(habits, list)
    assert habits[0]["name"] == "Чтение"

def test_log_habit_success(client):
    response = client.post("/habits/1/log", json={
        "date": str(date.today())
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Logged"

def test_log_habit_duplicate(client):
    response = client.post("/habits/1/log", json={
        "date": str(date.today())
    })
    assert response.status_code == 400
    assert "Already logged" in response.text

def test_log_habit_another_day(client):
    another_day = date.today() - timedelta(days=1)
    response = client.post("/habits/1/log", json={
        "date": str(another_day)
    })
    assert response.status_code == 200

def test_get_logs(client):
    response = client.get("/habits/1/logs")
    assert response.status_code == 200
    logs = response.json()
    assert isinstance(logs, list)
    assert "date" in logs[0]

def test_get_stats(client):
    response = client.get("/habits/1/stats")
    assert response.status_code == 200
    stats = response.json()
    assert "total_completions" in stats
    assert stats["total_completions"] >= 2

def test_log_invalid_habit(client):
    response = client.post("/habits/999/log", json={
        "date": str(date.today())
    })
    assert response.status_code in [404]