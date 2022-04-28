


def flatten(nested_array, i=0, acc=None) -> list:
  if acc == None:
    acc = []
  if not isinstance(nested_array, list) or i >= len(nested_array):
    return acc

  if isinstance(nested_array[i], int):
    acc.append(nested_array[i])
  elif isinstance(nested_array[i], list):
    flatten(nested_array[i], 0, acc)
  
  return flatten(nested_array, i + 1, acc)
