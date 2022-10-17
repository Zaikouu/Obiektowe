# def mult(*args):
#     suma = 1
#     for x in args:
#         for y in x:
#             suma *= y
#     return f'Iloczyn to : {suma}'
#
#
# def mult_ints(*args):
#     suma = 1
#     for x in args:
#         if isinstance(x, int):
#             suma *= x
#         else:
#             continue
#     return suma
#
#
# def multiply(*args):
#     suma = 1
#     for x in args:
#         suma *= x
#     return suma
#
#
# def make_car(firma, model, **kwargs):
#     dict_pom = {"Firma":firma, "Model":model}
#     for key, value in kwargs.items():
#         dict_pom[key] = value
#     return dict_pom
#
#
def main():
    # print(mult([3, 5, 7]))
    # print(mult(range(2, 8, 2)))
    # print(mult_ints(3, 3.14, 5, "abc", 7))
    # print(multiply(3, 5, 7))
    # print(make_car("toyota", "corolla", Poj_silnika=1.9, Rok_Produkcji=2000))
    # macierz = [[(x+1) for x in range(0, 10)],
    #            [(x+1)**2 for x in range(0, 10)],
    #            [(x+1)**3 for x in range(0, 10)]]
    # print(macierz)
    macierz_2 = [[] for x in range(0, 10)]
    suma = 0
    suma_2 = 0
    while suma < 10:
        while suma_2 <= suma:
            macierz_2[suma].append(suma_2+1)
            suma_2 += 1
        suma += 1
        suma_2 = 0
    print(macierz_2)
main()


