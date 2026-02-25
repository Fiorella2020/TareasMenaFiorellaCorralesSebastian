import pytest
def filtrar_vocales(cadena, bandera):
    # a) cadena debe ser string
    if not isinstance(cadena, str):
        return -100, None

    # c) cadena no debe estar vacía  (IMPORTANTE: antes de isalpha)
    if cadena == "":
        return -300, None

    # d) cadena no debe ser mayor a 30 caracteres
    if len(cadena) > 30:
        return -400, None

    # e) bandera debe ser booleano real (True/False)
    if type(bandera) is not bool:
        return -500, None

    # b) cadena debe contener solo letras
    if not cadena.isalpha():
        return -200, None

    vocales = "aeiouAEIOU"

    if bandera:
        filtrado = "".join(c for c in cadena if c in vocales)
    else:
        filtrado = "".join(c for c in cadena if c not in vocales)

    return 0, filtrado

def encontrar_extremos(lista):
    # a) Debe ser una lista
    if not isinstance(lista, list):
        return -600, None, None

    # c) No debe estar vacía
    if len(lista) == 0:
        return -800, None, None

    # d) No debe tener más de 15 elementos
    if len(lista) > 15:
        return -900, None, None

    # b) Todos deben ser números (int o float), pero NO bool
    for x in lista:
        if type(x) is bool or not isinstance(x, (int, float)):
            return -700, None, None

    # e) Retornar mínimo y máximo con código de éxito
    return 0, min(lista), max(lista)
