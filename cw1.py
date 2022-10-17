#Zadanie 1
#a)

# lista = []
# for x in range(1, 11):
#     lista.append(x)
# print(lista)

#b)

# lista = []
# for x in range(11):
#     lista.append(x*2)
# print(lista)

#c)

# lista = []
# for x in range(11):
#     lista.append(x**2)
# print(lista)

#d)

# lista = []
# for x in range(11,1):
#     lista.append(x*0)
# print(lista)

#e)

# lista = []
# for x in range(1,11):
#     if(x%2==0):
#         lista.append(1)
#     else:
#         lista.append(0)
# print(lista)

#f)

# lista = []
# for x in range(2):
#     for y in range(5):
#         lista.append(y)
# print(lista)

#Zadanie 2

#a)

# lista=[]
# suma=1
# while suma<11:
#     lista.append(suma)
#     suma+=1
# print(lista)

#b)

# lista = []
# suma = 0
# while suma<11:
#     lista.append(suma*2)
#     suma+=1
# print(lista)

#c)

# lista = []
# suma = 1
# while suma<11:
#     lista.append(suma**2)
#     suma+=1
# print(lista)

#d)

# lista = []
# suma = 1
# while suma<11:
#     lista.append(suma*0)
#     suma+=1
# print(lista)

#e)

# lista = []
# suma = 1
# while suma<11:
#     if(suma%2==0):
#         lista.append(1)
#     else:
#         lista.append(0)
#     suma+=1
# print(lista)

#f)

# lista = []
# x = 0
# y = 0
# while x < 2:
#     while y < 5:
#         lista.append(y)
#         y += 1
#     y = 0
#     x += 1
# print(lista)

#Zadanie 3

# def ile_ujemnych(lista):
#     suma_ujemnych = 0
#     for x in lista:
#         if(x < 0):
#             suma_ujemnych += 1
#     return suma_ujemnych
# lista = [ -3, 2, -5, 10, -2]
# print(ile_ujemnych(lista))

#Zadanie 4

# def iloczyn(lista):
#     suma = 1
#     for x in lista:
#         suma *= x
#     return suma
# lista = [3,4,20,5]
# print(iloczyn(lista))

#Zadanie 5

# def minmax(lista):
#     lista_pom = [min(lista), max(lista)]
#     return tuple(lista_pom)
# lista = [31,28,31,30,31,30,31,31,30,31,30,31]
# print(minmax(lista))

#Zadanie 6

# def suma_przemienna(lista):
#     suma = 0
#     for x in range(len(lista)):
#         if(x % 2 == 0):
#             suma += lista[x]
#         else:
#             suma -= lista[x]
#     return suma
# lista = [1, 4, 16, 9, 9, 7, 4, 9, 11]
# print(suma_przemienna(lista))

#Zadanie 7

lista = []
x = 0
while x<11:
   b = int(input())
   if(len(lista)>0):
        for y in lista:
            if(b==y):
                print('Ten element jest na liscie')
                break
            else:
                lista.append(b)
                x += 1
                break
   if(len(lista)==0):
        lista.append(b)
        x += 1
print(lista)