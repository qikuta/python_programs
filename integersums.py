"""
    Sum of Integers Up To n (integersums.py)

    Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero
    to the input parameter.

    The function should return 0 if a non-integer is passed in.
"""

user_in = input("enter an integer: ")

def add_it_up(num):
    sumnum = 0
    try:
        num = int(num)
    except:
        print("That's not an integer number.")
        quit()
    for i in range(num+1):
        sumnum += i
    return sumnum

print(add_it_up(user_in))





