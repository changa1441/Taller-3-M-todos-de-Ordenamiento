def insertion_sort(lista):
    """
    Método de Ordenamiento de Inserción (InsertionSort)

    El método de ordenamiento de inserción actúa recorriendo la lista a ordenar,
    tomando el elemento actual e insertándolo donde debería comparándolo con los
    elementos que ya ha recorrido.

    :param lista: La lista que se desea ordenar.
    :type lista: list
    :return: La lista ordenada.
    :rtype: list
    """
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

mi_lista = [12, 11, 13, 5, 6]
insertion_sort(mi_lista)
print("Lista ordenada:", mi_lista)
