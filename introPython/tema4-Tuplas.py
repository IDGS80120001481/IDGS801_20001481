'''
Las tuplas son inmutables
'''

tupla = ("uno", "dos", "tres") # Creacion de la tupla
print(tupla)

tuplasVarios = (12, True, 23.5, "El Gato", 12+4j)
print(tuplasVarios)

tuplasConTuplas = (1,2,3,4,(1,2,3))
print(tuplasConTuplas)

print(tuplasVarios[3])  # Entrar en un vaor especifico de una tupla
print(tuplasVarios[-2])
print(tuplasVarios[0:2])

a, b, c = tupla
print(a)
print(b)
print(c)

tuplasNueva = tupla+tuplasVarios
print(tuplasNueva)