numbers = [9, 2, 5, 3, 4, 1, 8, 6, 7]

def merge_sort(array):
  if len(array) == 1:
    return array

  #Recursively split arrays into half
  temparr1 = merge_sort(array[:len(array)//2])
  temparr2 = merge_sort(array[len(array)//2:])
  return merge(temparr1, temparr2)

def merge(array1, array2):
  outputarray = []
  x, y = 0, 0
  #Sort ascendingly by comparing values from both arrays
  while x < len(array1) and y < len(array2):
    if array1[x] < array2[y]:
      outputarray.append(array1[x])
      x += 1
    else:
      outputarray.append(array2[y])
      y += 1

  #Check for remaining, left-out array values
  while x < len(array1):
    outputarray.append(array1[x])
    x += 1

  while y < len(array2):
    outputarray.append(array2[y])
    y += 1

  return outputarray

print(merge_sort(numbers))
