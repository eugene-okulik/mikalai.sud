import pytest
import requests


@pytest.fixture()
def before_after():
    print("before test")
    yield
    print("after test")


@pytest.fixture(scope="session")
def start_end():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.mark.critical
@pytest.mark.medium
@pytest.mark.parametrize("test_data", [
    {"name": "name1", "data_name": "data_name1", "size": "size1"},
    {"name": "name2", "data_name": "data_name2", "size": "size2"},
    {"name": "name3", "data_name": "data_name3", "size": "size3"}
])
def test_r_post_create(test_data, start_end, before_after):
    body = {
        "name": test_data["name"],
        "data": {
            "color": "white",
            "size": test_data["size"],
            "id": 1,
            "name": test_data["data_name"]
        }
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://167.172.172.115:52353/object", json=body, headers=headers)
    assert response.status_code == 200


@pytest.fixture()
def data_for_test():
    body = {
        "name": "name",
        "data": {
            "color": "white",
            "size": "size",
            "id": 1,
            "name": "data_name"
        }
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://167.172.172.115:52353/object", json=body, headers=headers).json()
    created_id = response["id"]
    print(created_id)
    yield created_id
    try:
        check_response = requests.get(f"http://167.172.172.115:52353/object/{created_id}")
        if check_response.status_code == 200:
            requests.delete(f"http://167.172.172.115:52353/object/{created_id}")
    except:
        print(f"Could not check object {created_id}")


def test_r_delete(data_for_test):
    response = requests.delete(f"http://167.172.172.115:52353/object/{data_for_test}")
    assert response.status_code == 200


@pytest.mark.medium
def test_r_put(data_for_test):
    body = {
        "name": "justname",
        "data": {
            "color": "white-put",
            "size": "big-put",
            "id": 1,
            "name": "myobjeckt-put"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"http://167.172.172.115:52353/object/{data_for_test}", json=body, headers=headers)
    assert response.status_code == 200


def test_r_patch(data_for_test):
    body = {
        "name": "justname-patch",

    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f"http://167.172.172.115:52353/object/{data_for_test}", json=body, headers=headers)
    assert response.status_code == 200
    print(response.json())
