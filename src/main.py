from ydata.user import *
from ydata.room import *
import random

for i in range(1000):
    rooms = list_all_rooms()['rooms']
    random_user = random.randint(0, 14)
    random_room = random.randint(1, len('rooms') )
    random_action = random.randint(0, 6)
    match random_action:
        case 0:
            join_room(random_user, random_room)
        case 1:
            leave_room(random_user, random_room)
        case 2:
            create_room(random.randint(1, 12))
        case 3:
            delete_room(random_room)
        case 4:
            connect_as_admin("password")
        case 5:
            list_all_rooms()
        case 6:
            list_one_room(random_room)

print(list_all_rooms())