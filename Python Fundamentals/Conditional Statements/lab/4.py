"""
Write a Python program to check if a person is eligible to donate blood
using a nested if.

18 to 65 age  and more then 50kg weight person donate blood 
18
"""
name = input("Enter your name :")
age = int(input("ENter your age :"))
weight = int(input("Enter your weight : "))

if age <= 18 and age <= 65:
    if weight >= 50:
        print(f"{name} is eligible to donate blood")
else:
    print("this person not eligible to donate blood")