import pytest
from conftest import Yougile


base_url = "https://ru.yougile.com"


@pytest.mark.positive_test
def test_add_project():
    yougile = Yougile(
        "tatskaya.n@gmail.com", "ooosss2510", "c15cc9d0-2009-46b0-a800-46c1ae0000fd"
        )
    project_data = {
        "c15cc9d0-2009-46b0-a800-46c1ae0000fd": "admin"
    }
    response = yougile.create_project("Coding", project_data)

    assert "content" in response, "Expected 'content' in the response"
    assert len(response["content"]) > 0, "Expected content to have at least one project"
    project_id = response["content"][0]["id"]
    assert project_id is not None, "Expected project ID to be present"


@pytest.mark.positive_test
def test_get_list_of_projects():
    yougile = Yougile(
        "tatskaya.n@gmail.com", "ooosss2510", "c15cc9d0-2009-46b0-a800-46c1ae0000fd"
        )
    projects = yougile.get_list_of_projects()

    assert len(projects) > 0, "Projects list should not be empty"


@pytest.mark.positive_test
def test_update_project():
    yougile = Yougile(
        "tatskaya.n@gmail.com", "ooosss2510", "c15cc9d0-2009-46b0-a800-46c1ae0000fd"
        )

    project_name = "Test Project"
    project_data = {
        "c15cc9d0-2009-46b0-a800-46c1ae0000fd": "admin"
    }
    create_response = yougile.create_project(project_name, project_data)

    assert "content" in create_response, "Expected 'content' in the create response"
    assert len(create_response["content"]) > 0, "Expected content to have at least one project"

    project_id = create_response["content"][0].get("id")
    assert project_id is not None, "Expected project ID in the create response"

    new_title = "Updated Test Project"
    update_response = yougile.update_project(project_id, new_title)

    assert "id" in update_response, "Expected project ID in the update response"
    assert update_response.get("id") == project_id, "Expected project ID to match"


@pytest.mark.positive_test
def test_get_project_by_id():
    yougile = Yougile(
        "tatskaya.n@gmail.com", "ooosss2510", "c15cc9d0-2009-46b0-a800-46c1ae0000fd"
        )
    project_name = "Test Project"
    project_data = {
        "c15cc9d0-2009-46b0-a800-46c1ae0000fd": "admin"
        }
    create_response = yougile.create_project(project_name, project_data)
    print("Create response:", create_response)

    assert "content" in create_response, "Expected 'content' in the create response"
    assert len(create_response["content"]) > 0, "Expected content to have at least one project"
    project = create_response["content"][0]
    assert "id" in project, "Expected project ID in the create response"
    assert "title" in project, "Expected project title in the create response"
    project_id = project["id"]
    assert project_id is not None, "Expected project ID to be found in the create response"
    project_details = yougile.get_project_by_id(project_id)
    assert "id" in project_details, "Expected project ID in the project details response"
    assert "title" in project_details, "Expected project title in the project details response"
    assert project_details["id"] == project_id, "Project ID in details does not match the created project ID"


@pytest.mark.negative_test
@pytest.mark.xfail(
    reason="Expected ValueError when project name is missing."
    )
def test_add_project_missing_name():
    yougile = Yougile(
        "tatskaya.n@gmail.com",
        "ooosss2510",
        "c15cc9d0-2009-46b0-a800-46c1ae0000fd"
        )

    invalid_project_data = {
        "c15cc9d0-2009-46b0-a800-46c1ae0000fd": "admin"
    }

    with pytest.raises(ValueError, match="Project name is required."):
        yougile.create_project("", invalid_project_data)
        # Пустое имя проекта


@pytest.mark.negative_test
@pytest.mark.xfail(
    reason="Expected ValueError when users data is missing."
    )
def test_add_project_missing_users():
    yougile = Yougile(
        "tatskaya.n@gmail.com",
        "ooosss2510",
        "c15cc9d0-2009-46b0-a800-46c1ae0000fd"
        )

    with pytest.raises(ValueError,
                       match="Invalid user data format. Expected a dictionary with string values."
                       ):
        yougile.create_project("Test Project", None)
        # Отсутствие данных пользователей


@pytest.mark.negative_test
@pytest.mark.xfail(
    reason="Expected ValueError when users data format is invalid."
    )
def test_add_project_invalid_users_format():
    yougile = Yougile(
        "tatskaya.n@gmail.com",
        "ooosss2510",
        "c15cc9d0-2009-46b0-a800-46c1ae0000fd"
        )

    invalid_project_data = ["invalid_user_id"]
    # Неверный формат данных пользователей

    with pytest.raises(ValueError,
                       match="Invalid user data format. Expected a dictionary with string values."
                       ):
        yougile.create_project("Test Project", invalid_project_data)
        # Неверный формат данных пользователей