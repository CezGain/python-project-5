import requests

URL = "http://127.0.0.1:5000"

"""
for admin
"""


def create_room(nb_of_places: int) -> bool:
    url = URL + "/room/create"
    response = requests.post(url, json={"places": nb_of_places})
    if response.status_code == 200:
        return True
    return False


def delete_room(id: int) -> bool:
    url = URL + "/room/delete"
    response = requests.post(url, json={"id": id})
    if response.status_code == 200:
        return True
    return False


"""
for user
"""


def list_all_rooms():
    url = URL + "/rooms"
    return requests.get(url).json()


def list_one_room(id: int) -> tuple[bool, object]:
    url = f"{URL}/rooms/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        return True, response.json()
    return False
