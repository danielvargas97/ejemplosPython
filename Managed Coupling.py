#Managed coupling. We usally use DI(Injeccion de dependecias) to control coupling
# but in a weakly typed language it's different, we don't hate to create an
# interface or general class, classes and dependencies can be modified in
# ejecution time. This is an example.

class Transmision:
    pass

class Motor:  
    pass

class Vehiculo:
    def __init__(self, motor, transmision):
        self.transmision = transmision
        self.motor = motor
   
