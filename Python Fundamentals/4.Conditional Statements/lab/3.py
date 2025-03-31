"""
Write a Python program to calculate grades based on percentage using
if-else ladder.

"""
percentage = int(input("ENter the student percentage:-"))
if percentage >= 0 and percentage <= 100:
    if percentage >=90:
        print("A+ grade")
    elif percentage >=70 and percentage <90:
        print("B grade")
    elif percentage >=50 and percentage <70:
        print("c grade")
    elif percentage >=30 and percentage <50:
        print("d grade")
    else:
        print("file")
else:
    print("Enter the velid number ")