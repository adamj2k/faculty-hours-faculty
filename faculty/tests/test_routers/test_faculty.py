def test_get_teacher(client, create_sample_teacher):
    response = client.get(f"/faculty/teacher/{create_sample_teacher.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["last_name"] == "Doe"
    assert data["email"] == "john.doe@faculty.com"


def test_get_teacher_not_found(client):
    response = client.get("/faculty/teacher/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Teacher not found"


def test_create_teacher(client):
    response = client.post(
        "/faculty/teacher/create",
        json={
            "id": 2,
            "name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John"
    assert data["last_name"] == "Doe"
    assert data["email"] == "john.doe@example.com"


def test_create_teacher_invalid_data():
    # Test validation errors
    pass


def test_update_teacher_success():
    # Test successful update
    # Verify database changes
    # Verify message queue calls
    pass


def test_delete_teacher_success():
    # Test successful deletion
    # Verify database state
    # Verify message queue calls
    pass
