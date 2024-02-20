# PT-BR: 
#   Isso é um comentário e será ignorado pelo Python
#   Esse é um exemplo de um programa em Python que ensina como utilizar loops em python
# EN: 
#   This is a comment and will be ignored by Python.
#   This is an example of a Python program that show how use loops in python

print('---> for range: 0 - 4')
numbers = range(5)
# PT-BR: Imprime de 0 a 4 usando o for com o range
# EN: Print from 0 to 4 using for with range
for number in numbers:
  print(number)

print('---> for range: 1 - 5')
# PT-BR: Imprime de 1 a 5 usando o for com range
# EN: Print from 1 to 5 using for with range
for number in numbers:
  print(number+1)

print('---> while: 0 - 4')
# PT-BR: Imprime de 0 a 4 usando o while
# EN: Print from 0 a 4 using while
numbers = 0
while numbers < 5:
  print(numbers)
  numbers = numbers + 1

print('---> while: 5 - 1')
# PT-BR: Imprime de 5 a 1 usando o while
# EN: Print from 5 to 1 using while
while numbers > 0:
  print(numbers)
  numbers = numbers - 1

print('---> for list: 1 - 5')
# PT-BR: Imprime de 1 a 5 usando o for
# EN: Print from 1 to 5 using a for
list_numbers = [1, 2, 3, 4, 5]
for item in list_numbers:
  print(item)