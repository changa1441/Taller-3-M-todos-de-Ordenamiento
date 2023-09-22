def ordenamiento_shell(lista):
  """
  Ordena una lista usando el método de Shell.

  Args:
    lista: La lista a ordenar.

  Returns:
    La lista ordenada.
  """

  gap = len(lista) // 2
  while gap > 0:
    for i in range(gap, len(lista)):
      temp = lista[i]
      j = i
      while j >= gap and lista[j - gap] > temp:
        lista[j] = lista[j - gap]
        j -= gap
      lista[j] = temp
    gap //= 2

  return lista


if __name__ == "__main__":
  lista = [10, 5, 2, 7, 3, 9, 1, 6, 8]
  lista_ordenada = ordenamiento_shell(lista)
  print("Lista original:", lista)
  print("Lista ordenada:", lista_ordenada)
