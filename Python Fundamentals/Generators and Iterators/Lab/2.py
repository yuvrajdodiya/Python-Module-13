#• Write a Python program that uses a custom iterator to iterate over a list of integers


def integer_iterator(num):
    for i in num:
        yield i
        
num = [10,20,30,40,50]
iterator = integer_iterator(num)

for i in iterator:
    print(i)