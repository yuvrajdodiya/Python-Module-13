"""
• Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using
the break statement

"""
list1 = ['apple','mango','papaya','banana']
for fruit in list1:
    if fruit == 'banana':
        break
    #break satement is used to break loop.
    print(fruit)