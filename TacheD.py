'''
Écrivez une fonction Python qui prend en entrée une liste de dictionnaires représentant des
produits. Chaque dictionnaire a les clés "nom" (string), "prix" (float) et "quantite" (int). La
fonction doit trier la liste en fonction du prix de chaque produit, du moins cher au plus cher.
'''
def takePrix(value):
    return value["prix"]

def sortList(list = [{"nom": "fromage", "prix": 2.40, "quantite": 6},{"nom": "fraise", "prix": 0.50, "quantite": 100},{"nom": "manette", "prix": 24.99, "quantite": 4}]):
    list.sort(key=takePrix)
    return list;