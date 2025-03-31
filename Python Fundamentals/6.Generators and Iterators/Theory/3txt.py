""" Understanding iterators and creating custom iterators.

iterators ) An iterator is an object that allows you to traverse through all the elements of a
            collection, such as a list, tuple, or dictionary, one by one. Python provides a
            mechanism that makes iterating over objects easier.

"""


numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  
print(next(iterator))  
print(next(iterator))  
print(next(iterator))  
        