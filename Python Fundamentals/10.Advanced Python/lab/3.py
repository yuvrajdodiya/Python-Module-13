#• Write a Python program that filters out even numbers using the filter() function.
l1 = [23,34,45,67,23,98]

l2 = list(filter(lambda n : n%2==0 ,l1))
print(l2)   
