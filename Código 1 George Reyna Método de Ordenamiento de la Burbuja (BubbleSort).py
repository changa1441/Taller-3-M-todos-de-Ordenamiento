def ordenamiento_burbuja(lista):
  """
  Ordena una lista usando el método de la burbuja.

  Args:
    lista: La lista a ordenar.

  Returns:
    La lista ordenada.
  """

  for i in range(len(lista) - 1):
    for j in range(len(lista) - i - 1):
      if lista[j] > lista[j + 1]:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]

  return lista


if __name__ == "__main__":
  lista = [10, 5, 2, 7, 3, 9, 1, 6, 8]
  lista_ordenada = ordenamiento_burbuja(lista)
  print("Lista original:", lista)
  print("Lista ordenada:", lista_ordenada)
