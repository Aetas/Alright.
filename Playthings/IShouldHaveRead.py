# if I had just read the paragraph below fib(), I would have seen the answer to my own question.
# Which is that functions always return None unless otherwise specified, making them procedures rather than functions.
# Which is why print is so heavily used. I guess there had better be a cprint() then.

def fib(n): # It's annoying that 'in' is a reserved word.
    """Fibonacci probably made good pasta"""
    result = [] # can I use None in here? No, it puts None as the first element.
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print("fib: ", fib(2000))
fib(2000) # should this even print anything? Maybe. That's the scripting stuff for you.
fn = fib(2000)
print("fn:  ",fn)

# it's funny how even though this is a direct script, there is a small layer
# between the script and the interpreter because things like typing "fn" plain
# doesn't return anything
