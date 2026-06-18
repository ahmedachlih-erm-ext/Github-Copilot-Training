def test_get_activities_returns_all_activities(client, sample_activities):
    # Arrange
    expected_activities = sample_activities

    # Act
    response = client.get("/activities")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert body == expected_activities
    assert len(body) == len(expected_activities)


def test_get_activities_response_structure(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(body, dict)
    assert "Chess Club" in body

    activity = body["Chess Club"]
    assert set(activity.keys()) == expected_keys
    assert isinstance(activity["participants"], list)
    assert isinstance(activity["max_participants"], int)
