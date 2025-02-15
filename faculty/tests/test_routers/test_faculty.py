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


def test_create_teacher_invalid_data(client):
    # Test missing required fields
    response = client.post(
        "/faculty/teacher/create",
        json={
            "name": "John",
            "last_name": "Doe"
            # missing email and id
        },
    )
    assert response.status_code == 422

    # Test invalid email format
    response = client.post(
        "/faculty/teacher/create",
        json={"id": 1, "name": "John", "last_name": "Doe", "email": "invalid-email"},
    )
    assert response.status_code == 422

    # Test invalid ID type
    response = client.post(
        "/faculty/teacher/create",
        json={
            "id": "not-a-number",
            "name": "John",
            "last_name": "Doe",
            "email": "john.doe@faculty.com",
        },
    )
    assert response.status_code == 422


def test_update_teacher_success(client, create_sample_teacher):
    # Test successful update
    updated_data = {
        "id": create_sample_teacher.id,
        "name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@faculty.com",
    }

    response = client.put(
        f"/faculty/teacher/update/{create_sample_teacher.id}", json=updated_data
    )

    assert response.status_code == 200
    data = response.json()

    # Verify response data
    assert data["name"] == updated_data["name"]
    assert data["last_name"] == updated_data["last_name"]
    assert data["email"] == updated_data["email"]

    # Verify database changes by fetching the updated teacher
    get_response = client.get(f"/faculty/teacher/{create_sample_teacher.id}")
    updated_teacher = get_response.json()

    assert updated_teacher["name"] == "Jane"
    assert updated_teacher["last_name"] == "Smith"
    assert updated_teacher["email"] == "jane.smith@faculty.com"


def test_delete_teacher_success(client, create_sample_teacher):
    # Verify teacher exists before deletion
    get_response = client.get(f"/faculty/teacher/{create_sample_teacher.id}")
    assert get_response.status_code == 200

    # Test successful deletion
    response = client.delete(f"/faculty/teacher/delete/{create_sample_teacher.id}")
    assert response.status_code == 204
