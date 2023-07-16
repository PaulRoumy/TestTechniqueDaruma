import flask
from flask import request

'''
    Tache A
    Écrivez une API RESTful en Utilisant le framework Flask qui explose les fonctionnalités suivantes :

    ● Une route GET "/users" qui renvoie la liste de tous les utilisateurs.

    ● Une route GET "/users/{id}" qui renvoie les détails d'un utilisateur spécifique en
    fonction de son ID.

    ● Une route POST "/users" qui permet de créer un nouvel utilisateur avec les données
    fournies en JSON.

    ● Une route PUT "/users/{id}" qui permet de mettre à jour les informations d'un
    utilisateur spécifique en fonction de son ID avec les données fournies en JSON.

    ● Une route DELETE "/users/{id}" qui permet de supprimer un utilisateur spécifique en
    fonction de son ID.
'''
app = flask.Flask("Tache A")
app.config["Debug"] = True

listUser = [{'id': 0,'name': 'Paul'},{'id':1,'name':'Jean'}]

# return all user in list
@app.route('/users', methods= ['GET'])
def getAllUser():
    return listUser

# return user with correct id
@app.route('/users/<id>', methods= ['GET'])
def getOneUserById(id):
    for user in listUser:
        if user.get('id') == id:
            return user

# add user in list from json
@app.route('/users', methods= ['POST'])
def addUser():
    listUser.insert(
        {'id': request.json['id'], 'name': request.json['name']}
    )

# modify user with correct id with a json
@app.route('/users/<id>', methods= ['PUT'])
def modifyUser(id):
    for user in listUser:
        if user.get('id') == id:
            user.id = request.json['id']
            user.name = request.json['name']

# delete user with correct id
@app.route('/user/<id>', methods= ['DELETE'])
def deleteUser(id):
    for user in listUser:
        if user.get('id') == id:
            listUser.remove(user)
