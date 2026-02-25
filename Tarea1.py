def filtrar_vocales(cadena, bandera):
    # a) cadena debe ser string
    if not isinstance(cadena, str):
        return -100, None

    # b) cadena debe contener solo letras del abecedario
    if not cadena.isalpha():
        return -200, None
    
    # c) cadena no debe estar vacía
    if cadena == "":
        return -300, None

    # d) cadena no debe ser mayor a 30 caracteres
    if len(cadena) > 30:
        return -400, None

    # e) bandera debe ser booleano real (True/False)
    # OJO: bool es subclase de int, por eso usamos type(...) is bool
    if type(bandera) is not bool:
        return -500, None

    # f y g) filtrar según bandera
    vocales = "aeiouAEIOU"

    if bandera is True:
        filtrado = "".join(car for car in cadena if car in vocales)
    else:
        filtrado = "".join(car for car in cadena if car not in vocales)

    # h + i) código de éxito + string filtrado
    return 0, filtrado