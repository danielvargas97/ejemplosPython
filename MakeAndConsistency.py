##Make common things easy and rare things possible
##Consistency

##Sometimes we need to change our code, so it's neccesary that the code
##be smple and easier to understand an use.Also Extend help us to have consistency in our code.


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    

class Jugador(Persona):
    def __init__(self, nombre, numero):
        Persona.__init__(self,nombre)
        self.numero = numero
    
    def nombreJugador(self):
        return self.getNombre()
    
    def getNumeroJugador(self):
        return self.numero

class Equipo:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        
    def impEquipo(self):
        print "Equipo ", jugador1.getNombre()," y ", jugador2.nombreJugador()
    

if __name__ == "__main__":
    jugador1 = Jugador("Messi","10")
    jugador2 = Jugador("Cristiano","7")
    equipo = Equipo(jugador1,jugador2)
   
    print "Nombre de jugador: " , jugador1.nombreJugador() , ", Numero: ",jugador1.getNumeroJugador()
    print "Nombre de jugador: " , jugador2.nombreJugador() , ", Numero: ",jugador2.getNumeroJugador()
    equipo.impEquipo()


    
