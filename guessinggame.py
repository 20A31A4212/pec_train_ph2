#Guessing game
from random import randint

num = randint(1, 50)
chance = 5
while chance != 0:
  n = int(input('Guess:'))
  if n == num:
    print('You won')
    break
  elif n < num:
    print(n, 'is smaller than the actual number')
  else:
    print(n, 'is greater than the actual number')
  chance -= 1
print(num)