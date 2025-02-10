#Practical Example 6: Write a Python program to check if a number is prime using if_else.
num = int(input("Enter the number:-"))
count = 0 
for i in range(2,num):
    if num%1 == 0:
        count +=1
    if count==0:
        print(f"{num} is prime number")
    else:
        print(f"{num} is not prime number ") 