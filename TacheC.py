'''
Écrivez une classe Python qui représente un système de cache simple. Le cache doit avoir
les fonctionnalités suivantes :
    ● Un attribut "capacite" qui représente la capacité maximale du cache.
    ● Une méthode "ajouter" qui permet d'ajouter une clé et une valeur au cache. Si le
    cache atteint sa capacité maximale, la méthode doit supprimer la plus ancienne clé
    ajoutée avant d'ajouter la nouvelle clé et valeur.
    ● Une méthode "obtenir" qui renvoie la valeur associée à une clé donnée. Si la clé
    n'existe pas dans le cache, la méthode doit renvoyer None.
'''

class Cache:
    capacite = 4
    cache = []
    def ajouter(self, key, value):
        if len(self.cache) == self.capacite:
            self.cache.pop(0)
        self.cache.append({'key': key, 'value': value})

    def find(self, key):
        for object in self.cache:
            if object['key'] == key :
                return object['value']
            return "None"


