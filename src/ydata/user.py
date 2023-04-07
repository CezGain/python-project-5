import requests

URL = "http://127.0.0.1:5000"

""""
for admin
"""


def connect_as_admin(password: str) -> bool:
    url = URL + "/admin/connection"
    response = requests.post(url, json={"password": password})
    if response.status_code == 200:
        return True
    return False


"""
for all
"""


def join_room(user_id: int, room_id: int) -> tuple[bool, str]:
    url = URL + "/room/join"
    response = requests.post(
        url, json={"user_id": user_id, "room_id": room_id})
    if response.status_code == 200:
        data = response.json()
        if "estimed_waiting" in data:
            return True, f"Estimated waiting time {data['estimed_waiting']}"
        return True, "Room joined succesfully"
    return False


def leave_room(user_id: int, room_id: int) -> bool:
    url = URL + "/room/leave"
    response = requests.post(
        url, json={"user_id": user_id, "room_id": room_id})
    if response.status_code == 200:
        return True
    return False
