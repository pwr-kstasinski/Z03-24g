def sortuj(lista: list, *reszta):
    lista += list(reszta)
    lista.sort()
    return lista
