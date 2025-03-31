#• Write a generator function that generates the first 10 even numbers.
def even_numbers():
    num = 0
    for i in range(1, 11):  
        yield num
        num += 2      


# Using the generator:
for num in even_numbers():
    print(num)
