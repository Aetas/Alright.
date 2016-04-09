# time to chain some useless functions to see if I can get python to complain.

def get_input():
    start = input("Gimme a number: ")
    return start

def do_something(n):
    a = 0
    while n % 2 != 0:
        n = n % 2
        # a++ # <-- doesn't work. Whyyyyy.
        a += 1 # at least this works
    return a

def intermediate(n):
    if n == 0:
        return 0
    elif n  == 1:
        return 1
    elif n == 8:
        return 2
    elif n > 0: # I'm using in > 0 instead of > 1 just to test if Python will keep my order or respect my wishes
        return 3
    else:
        return 4
    return 5 # I wonder if this will cause any problems.

def determine(n): # this will test how python stores argument variables for functions and their scope
    if n == 0:
        print("That number wasn't even divisible by 2.")
    elif n  == 1:
        print("That number was, in fact, 2.")
    elif n == 2:
        print("That number was 16.")
    elif n == 3: # I'm using in > 0 instead of > 1 just to test if Python will keep my order or respect my wishes
        print("That number was greater than 2 and even!")
    else: # should be 4 case, but 5 will be caught, too
        print("How did you get here? Seriously.")
    return n # I wonder if this will cause any problems.

determine(intermediate(do_something(get_input())))
