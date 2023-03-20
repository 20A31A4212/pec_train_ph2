#binary search using recursion
a = 0


def binarySearch(l, low, high, key):
  mid = (low + high) // 2
  if l[mid] == key:
    print('Element found at', mid)
    a = 1
    return a
  elif l[mid] > key:
    high = mid - 1
  elif l[mid] < key:
    low = mid + 1
  return binarySearch(l, low, high, key)


l = [1, 2, 3, 4, 5]
key = 5
high = len(l) - 1
low = 0
a = binarySearch(l, low, high, key)
if a == 0:
  print('Element not found')