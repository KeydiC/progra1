class Perro():
    tipo="Perro"
    def __init__(self, nom,col):
        self.nom=nom
        self.color=col
    def sonido(self):
        return ("woof!!")

class Gato():
    tipo="Gato"
    def __init__(self, nom, col):
        self.nom=nom
        self.color=col
    def sonido(self):
        return ("meow!!")
    
class Pez():
    tipo="Pez"
    def __init__(self, nom, col):
        self.nom=nom
        self.color=col
    def sonido(self):
        return ("gloop!!")
