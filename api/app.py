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

listSalle = [{
    'Salle-id': 0,
    'Name': "Issou",
    'Place': 5,
    'Joueur': 1
},
{
    'Salle-id': 1,
    'Name': "Issou",
    'Place': 2,
    'Joueur': 2
},
{
    'Salle-id': 2,
    'Name': "Issou",
    'Place': 4,
    'Joueur': 3
},
{
    'Salle-id': 3,
    'Name': "Issou",
    'Place': 3,
    'Joueur': 1
},
{
    'Salle-id': 4,
    'Name': "Issou",
    'Place': 10,
    'Joueur': 6
}]

PlayerList = [{
    'PlayerId': 0,
    'SalleId': None,
    'Name': 'feur'
},
{
    'PlayerId': 1,
    'SalleId': None,
    'Name': 'feur1'
},
{
    'PlayerId': 2,
    'SalleId': None,
    'Name': 'feur2'
}]



@app.route("/listSalle")
def allSalle():
    return dict(message=listSalle)




@app.route("/Salle-id", methods = ['GET', 'POST', 'DELETE'])
def bySalleId():
    if request.method == 'GET':
        id = request.args.get('id')
        return dict(salle_id=listSalle[int(id)]['Salle-id'])
    if request.method == 'POST':
        place = request.args.get('place')
        name = request.args.get('name')
        newPlace = {
                'Salle-id': len(listSalle),
                'Name': name,
                'Place': place,
                'Joueur': 0
        }
        listSalle.append(newPlace)
        return dict(salleadd = newPlace)
    if request.method == 'DELETE':
        id = request.args.get('id')
        listSalle.pop(int(id))
        return dict(Succes = "True")



@app.route("/join")
def join():
    idSalle = request.args.get('idSalle')
    PlayerId = request.args.get('PlayerId')
    if (listSalle[int(idSalle)]['Joueur'] == listSalle[int(idSalle)]['Place'] and PlayerList[int(PlayerId)]['SalleId'] != None):
        return dict(Succes = "Complete or Already in a salle")
    else:
        listSalle[int(idSalle)]['Joueur'] += 1
        PlayerList[int(PlayerId)]['SalleId'] = idSalle
        return dict(Succes = 'You join')
    


@app.route("/Left")
def left():
    PlayerId = request.args.get('PlayerId')
    if ( PlayerList[int(PlayerId)]['SalleId'] == None):
        return dict(Succes = "Join before leave")
    else:
        listSalle[int(PlayerList[int(PlayerId)]['SalleId'])]['Joueur'] -= 1
        PlayerList[int(PlayerId)]['SalleId']= None
        return dict(Succes = 'You Left')
    