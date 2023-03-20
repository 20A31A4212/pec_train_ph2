#Binary search using normal method
l = [1, 2, 3, 4, 5]
a = 5
high = len(l) - 1
low = 0
b = 0
while low <= high:
  mid = (low + high) // 2
  if l[mid] == a:
    print('Element found at', mid)
    b = 1
    break
  elif l[mid] > a:
    high = mid - 1
  elif l[mid] < a:
    low = mid + 1
if b == 0:
  print('Element not found')