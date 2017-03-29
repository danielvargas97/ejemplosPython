class Singleton(type):
 
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)
 
    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args,**kw)
        return cls.__instance

class A(object):
        
    __metaclass__ = Singleton
        
    
a = A()
b = A()
print(a == b)

#Retorna true en caso de que ambas sean iguales, la misma
#instancia
