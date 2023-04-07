"""
Launch from the project directory with
> python -m flask --app api/app.py run
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    """
    This hello world function is a simple example of endpoint.
    """
    return dict(message="Hello World!")


list_rooms = [
    {
        "id": 1,
        "places": 2,
        "users_id": [1, 5],
        "users_waiting": []
    },
    {
        "id": 2,
        "places": 3,
        "users_id": [8, 3, 4],
        "users_waiting": []
    },
    {
        "id": 3,
        "places": 5,
        "users_id": [9, 6],
        "users_waiting": []
    },
]

list_users = [
    {
        "id": 0,
        "username": "admin",
        "creation_date": "2023-04-06 09:00:00",
        "last_time_connected": "connected",
        "since_connection": 124,
        "time_connected_average": 154,
        "number_of_times_connected": 5
    },
    {
        "id": 1,
        "username": "User1",
        "creation_date": "2023-04-06 09:31:52",
        "last_time_connected": "connected",
        "since_connection": 265,
        "time_connected_average": 781,
        "number_of_times_connected": 3
    },
    {
        "id": 2,
        "username": "User2",
        "creation_date": "2023-04-06 09:45:07",
        "last_time_connected": "2023-04-06 17:34:14",
        "since_connection": 0,
        "time_connected_average": 145,
        "number_of_times_connected": 6
    },
    {
        "id": 3,
        "username": "User3",
        "creation_date": "2023-04-06 10:12:35",
        "last_time_connected": "connected",
        "since_connection": 41,
        "time_connected_average": 458,
        "number_of_times_connected": 14
    },
    {
        "id": 4,
        "username": "User4",
        "creation_date": "2023-04-06 10:21:45",
        "last_time_connected": "connected",
        "since_connection": 457,
        "time_connected_average": 245,
        "number_of_times_connected": 9
    },
    {
        "id": 5,
        "username": "User5",
        "creation_date": "2023-04-06 10:48:20",
        "last_time_connected": "connected",
        "since_connection": 120,
        "time_connected_average": 471,
        "number_of_times_connected": 9
    },
    {
        "id": 6,
        "username": "User6",
        "creation_date": "2023-04-06 11:05:14",
        "last_time_connected": "connected",
        "since_connection": 987,
        "time_connected_average": 1245,
        "number_of_times_connected": 7
    },
    {
        "id": 7,
        "username": "User7",
        "creation_date": "2023-04-06 11:15:25",
        "last_time_connected": "2023-04-06 17:34:14",
        "since_connection": 0,
        "time_connected_average": 423,
        "number_of_times_connected": 2
    },
    {
        "id": 8,
        "username": "User9",
        "creation_date": "2023-04-06 11:42:01",
        "last_time_connected": "connected",
        "since_connection": 245,
        "time_connected_average": 0,
        "number_of_times_connected": 0
    },
    {
        "id": 9,
        "username": "User9",
        "creation_date": "2023-04-06 11:54:35",
        "last_time_connected": "connected",
        "since_connection": 834,
        "time_connected_average": 918,
        "number_of_times_connected": 4
    },
]


@app.route("/rooms", methods=["GET", "POST"])
def get_all_rooms():
    """
    Return all rooms informations
    """
    return dict(
        numbers_of_rooms=len(list_rooms),
        rooms=list_rooms,
    )


@app.route("/rooms/<int:id>", methods=["GET", "POST"])
def get_room_info(id: int):
    """
    Return the information of one room or an error
    """
    for room in list_rooms:
        if room["id"] == id:
            return room, 200
    return dict(error_msg="room not found"), 404


@app.route("/room/join", methods=["POST"])
def post_room_join():
    """
    Connect the user to the room, or return waiting times or an error
    """
    input_data = request.json
    try:
        assert "room_id" in input_data
        room_id = int(input_data["room_id"])
        assert "user_id" in input_data
        user_id = int(input_data["user_id"])
    except Exception:
        return dict(error_msg="wrong or missing arguments \"room_id\" or \"user_id\""), 400
    for i, room in enumerate(list_rooms):
        if room["id"] == room_id:
            users_in_room = room["users_id"]
            if room["places"] <= len(users_in_room):
                list_rooms[i]["users_waiting"].append(user_id)
                waiting_time = 0
                for user in users_in_room:
                    for user_info in list_users:
                        if user == user_info["id"]:
                            time = user_info["time_connected_average"] - \
                                user_info["since_connection"]
                            if time < 0:
                                time = 0
                            waiting_time += time
                            break
                waiting_time //= len(list_users)
                return dict(estimed_waiting=f"{waiting_time} seconds"), 200
            else:
                list_rooms[i]["users_id"].append(user_id)
                return dict(joined="you have joined the room"), 200
    return dict(not_found="room not found"), 404


@app.route("/room/leave", methods=["POST"])
def post_room_leave():
    input_data = request.json
    try:
        assert "room_id" in input_data
        room_id = int(input_data["room_id"])
        assert "user_id" in input_data
        user_id = int(input_data["user_id"])
    except Exception:
        return dict(error_msg="wrong or missing arguments \"room_id\" or \"user_id\""), 400
    for i, room in enumerate(list_rooms):
        if room["id"] == room_id:
            for j, id in enumerate(room["users_id"]):
                if id == user_id:
                    list_rooms[i]["users_id"].pop(j)
                    return dict(success="user left with success"), 200
            for j, id in enumerate(room["users_waiting"]):
                if id == user_id:
                    list_rooms[i]["users_waiting"].pop(j)
                    return dict(success="user left with success"), 200
            return dict(not_found="user not found"), 404
    return dict(not_found="room not found"), 404


@app.route("/room/create", methods=["POST"])
def room_create():
    input_data = request.json
    try:
        assert "places" in input_data
        nb_of_places = int(input_data["places"])
    except Exception:
        return dict(error_msg="wrong or missing arguments \"places\""), 400
    list_rooms.append({
        "id": list_rooms[len(list_rooms) - 1]["id"] + 1,
        "places": nb_of_places,
        "users_id": []
    })
    return dict(created="room create with success"), 200


@app.route("/room/delete", methods=["POST"])
def room_delete():
    input_data = request.json
    try:
        assert "id" in input_data
        id = int(input_data["id"])
    except Exception:
        return dict(error_msg="wrong or missing arguments \"id\""), 400
    for i, room in enumerate(list_rooms):
        if room["id"] == id:
            list_rooms.pop(i)
            return dict(deleted="room delete with success"), 200
    return dict(error_msg="ressource not found"), 404


@app.route("/admin/connection", methods=["POST"])
def connect_as_admin():
    input_data = request.json
    try:
        assert "password" in input_data and input_data["password"] == "password"
    except Exception:
        return dict(error_msg="wrong or missing arguments \"password\""), 400
    return dict(success="you are connected as admin"), 200
