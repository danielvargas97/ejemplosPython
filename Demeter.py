#Ejemplo Demeter en Python#

class Equipo(object):
    def __init__(self,name):
        self.name = name


    def nameEquipo(self):
        return self.name


class Torneo(object):
    def __init__(self,equipo):
        self.equipo = equipo


    def imprimeDataAlt(self,nameTeam):
        print(nameTeam)

if __name__ == "__main__":
    a = Equipo("Colombia")
    x = Torneo(a)

    print(x.equipo.nameEquipo())
    x.imprimeDataAlt(a.nameEquipo())
