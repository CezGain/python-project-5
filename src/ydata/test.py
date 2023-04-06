import requests

URL = "http://127.0.0.1:5000/"

def listSalle():
    response = requests.get(URL+"listSalle")

    data = response.json()

    print(data)

    return data

listSalle()

def Salle_id(id):
    response = requests.get(URL+"Salle-id?id="+str(id))

    data = response.json()

    print(data)

    return data

Salle_id(1)


def join(id, player):
    response = requests.get(URL+"join?idSalle="+str(id)+"&PlayerId="+str(player))

    data = response.json()

    print(data)

    return data

join(1,1)

def Left(player):
    response = requests.get(URL+"Left?PlayerId="+str(player))

    data = response.json()

    print(data)

    return data

Left(1)