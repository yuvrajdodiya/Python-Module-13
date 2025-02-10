#• Write a Python program to apply the map() function to square a list of numbers.

l1 = [1,2,3,4,5]

def square(n):
    return n*n

l2 = list(map(square,l1))

print(l2)