def test_signup_for_activity_succeeds(client):
    # Arrange
    email = "new.student@mergington.edu"
    endpoint = "/activities/Chess Club/signup"

    # Act
    response = client.post(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}

    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]


def test_signup_for_existing_student_returns_400(client):
    # Arrange
    email = "michael@mergington.edu"
    endpoint = "/activities/Chess Club/signup"

    # Act
    response = client.post(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"


def test_signup_for_missing_activity_returns_404(client):
    # Arrange
    endpoint = "/activities/Nonexistent Activity/signup"
    email = "student@mergington.edu"

    # Act
    response = client.post(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_requires_email_parameter(client):
    # Arrange
    endpoint = "/activities/Chess Club/signup"

    # Act
    response = client.post(endpoint)

    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()
