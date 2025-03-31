""" Understanding how generators work in Python.


**        A generators are a type of iterable, like lists or tuples, but unlike lists, they do
          not store all the values in memory  a generator produces items one at a time, only when they are needed

"""
my_list = [1, 2, 3, 4, 5]
new_list = [x * x for x in my_list if x % 2 != 0]
print(new_list)