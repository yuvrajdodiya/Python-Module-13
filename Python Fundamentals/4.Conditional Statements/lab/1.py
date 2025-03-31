#Write a Python program to find greater and less than a number using if_else.

num1 = int(input("Enter the number1 :-"))
num2 = int(input("Enter the number2 :-"))
if num1 > num2:
    print(f"{num1} is greater then {num2}")
elif num1 < num2:
    print(f"{num1} is less then {num2}")
else:
    print(f"{num1} and {num2} is equal.")