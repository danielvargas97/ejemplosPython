#-*- coding:utf-8 -*-#


class Lista(object):
    def __init__(self):
        self.lista = []

    def agregar(self,x):
        self.lista.append(x)

    def ordenar(self):
        pass

    def ver_lista(self):
        print (self.lista)




class Lista_General(Operacion):
    def __init__(self):
        super().__init__()

    def ordenar(self):
        for i in range(len(self.lista)):
            for j in range(i,len(self.lista)):
                 if self.lista[i] < self.lista[j]:
                     self.lista[j],self.lista[i] = self.lista[i],self.lista[j]

    def ordenar_reverso(self):
        for i in range(len(self.lista)):
            for j in range(i,len(self.lista)):
                 if self.lista[i] > self.lista[j]:
                     self.lista[j],self.lista[i] = self.lista[i],self.lista[j]


    def limpiar(self):
        
        for i in range(0,len(self.lista)):
            self.lista.pop(i)


class Lista_Simple(Operacion):
    def __init__(self):
        super().__init__()

    def ordenar(self):
        self.lista.sort(reverse=True)
        

    
if __name__ == "__main__":
    lista = [11,4,52,33,14,-6,-54]

    #Creando objeto simple#
    simple = Lista_Simple()
    
    #Creando objeto General#
    general = Lista_General()

    #Rellenando datos en los objetos#
    for i in range(0,len(lista)):
        simple.agregar(lista[i])
        general.agregar(lista[i])


    #Cada uno llama a su metodo ordenar#
    simple.ordenar()
    general.ordenar()


    #Muestra las listas ordenadas#
    #Solo se necesitaba la mas simple de ellas para resolver el problema#
    simple.ver_lista()
    general.ver_lista()
    
    


    
    
