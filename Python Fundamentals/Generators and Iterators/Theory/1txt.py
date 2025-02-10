""" Understanding how generators work in Python.
        A generators are a type of iterable, like lists or tuples, but unlike lists, they do
not store all the values in memory  a generator produces items one at a time, only when they are needed

"""
def generator(n):
  for i in range(n):
    yield i

# Create a generator object
gen = generator(5)

# Get values one by one
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

# Use in a loop
for value in gen:
  print(value)    # Output: 3, 4