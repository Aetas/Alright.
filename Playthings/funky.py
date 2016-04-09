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

    
