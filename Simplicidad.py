#Simplicidad de python al querer calcular un numero mayor

mayor=0
vector=[]

print "Ingrese 5 numeros:"
for i in range(0,5):
    numero=int(raw_input('Ingrese #  '+str(i+1)+': '))
    vector.append(numero)
print vector

for v in vector:
    if mayor<v:
        mayor=v#se guarda el numero mayor

print 'El mayor es: ',mayor # resultado
