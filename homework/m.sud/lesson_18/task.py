import requests


def r_post():
    body = {
        "name": "justname",
        "data": {
            "color": "white",
            "size": "big",
            "id": 1,
            "name": "myobjeckt"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://167.172.172.115:52353/object", json=body, headers=headers).json()
    print(response)


def r_put():
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
    response = requests.put("http://167.172.172.115:52353/object/12490", json=body, headers=headers).json()
    print(response)


def r_patch():
    body = {
        "name": "justname-patch",

    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch("http://167.172.172.115:52353/object/12490", json=body, headers=headers).json()
    print(response)


def first_posts():
    response = requests.get("http://167.172.172.115:52353/object/1").json()
    print(response)


def r_delete():
    response = requests.delete("http://167.172.172.115:52353/object/12495")
    print(response.status_code)


r_post()
first_posts()
r_put()
r_patch()
r_delete()
