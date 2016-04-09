# finally something other than a script
# though, let's be honest it's better than the mathematica kernel (which wasn't intended to be used like python)
# and is a good script layer, I imagine.
# if only I was using bash/shell right now, I'd cat that script layer all day.
# also vim.

# Will python bitch about that space?

# functions:

def fib(n):
    """What does this do?"""
    a, b = 0, 1 # I have misgivings about that syntax choice but what do I know?
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

# update: python doesn't give a damn about those empty lines. Though atom might just be humoring me and not actually putting carriage returns there.

fn = fib
fn(1500)

tst = fib(2000)
# I guess that one was an obvious result
print(tst) # why do you return as none?
# and why does assigning a new variable to a function return call the function?
# I guess it has to do with the fact that the only output is actually a print and not a number return.
# and in that guess I had assumed that these outputs were stores as a ASCII char output rather than an integer-like type.
# C might have called me stupid in this case but at least I would have learned something from it.
# such as where to go next.
# C++: "You're stupid for trying to assign incompatible data types, do it right"
# Python: "Shh, bb I'll take care of you until I fail spectacularly and refuse to tell you what happened"

# the fact that this automatically return-lines is going to irk me at some point

# some return type testing.

def first_integer_test(a):
    return a # so return() is a thing. Good.

fn(first_integer_test(2000))

# surely we can go deeper, this is supposed to be a nice functional language, right? Right?

def grab(): # it has no argument. Gucci?
    in = input()
    return in

external = 0

def ext_grab():
    c = input()
    external = c
    return c

fn(ext_grab())
