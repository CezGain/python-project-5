from ydata.user import *
from ydata.room import *
import random

rooms_create = 0
rooms_delete = 0
rooms_join = 0
rooms_leave = 0
count_admin = 0

for i in range(500):
    rooms = list_all_rooms()['rooms']
    random_user = random.randint(0, 14)
    random_room = random.randint(1, len('rooms'))
    random_action = random.randint(0, 6)
    match random_action:
        case 0:
            join_room(random_user, random_room)
            rooms_join += 1
        case 1:
            leave_room(random_user, random_room)
            rooms_leave += 1
        case 2:
            create_room(random.randint(1, 12))
            rooms_create += 1
        case 3:
            delete_room(random_room)
            rooms_delete += 1
        case 4:
            connect_as_admin("password")
            count_admin += 1
        case 5:
            list_all_rooms()
        case 6:
            list_one_room(random_room)


print(list_all_rooms())
print("---------------\n")

print("Nombre de rooms: ", len(list_all_rooms()['rooms']))
print("Nombre de rooms crées: ", rooms_create)
print("Nombre de rooms suprimés: ", rooms_delete, "\n")

print("Nombre de rooms rejoint: ", rooms_join)
print("Nombre de rooms leave: ", rooms_leave, "\n")

print("Nombre de passage admin: ", count_admin, "\n")
