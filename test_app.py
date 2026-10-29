from app import app

def test_calc():
    client = app.test_client()
    res = client.get('/calculate?marks=80&marks=90&marks=70')
    assert "Total: 240.0" in res.text
    assert "Average: 80.0" in res.text
    assert "Grade: B" in res.text
