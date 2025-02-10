#• Practical Example 1: How does the Python code structure work?

mark = int(input("Enter the marks :"))
if mark >= 50 and mark <= 100:
    print("A grade")
elif mark >=30 and mark < 50:
    print("B grade")
else:
    print("file ")


"""
     input() is used to get input from the user.
     int(input()) converts the input (a string) into an integer.
     if checks if the condition (mark >= 50 ) is true.
     if true, it prints "A grade "Otherwise, the else block runs.
     Python is an interpreted language, which means it processes and executes code line by line.
"""