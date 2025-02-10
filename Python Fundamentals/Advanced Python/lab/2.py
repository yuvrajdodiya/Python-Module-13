#• Write a Python program that uses reduce() to find the product of a list of numbers.
from functools import reduce
def product(number):
    return 1

numbers = [1, 2, 3, 4]
result = reduce(product, numbers, 100) 
print(result) 