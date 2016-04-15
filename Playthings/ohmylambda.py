# time to do some of them lambda/closure functions n such.
# Also, VisualStudio Code?
# On a side note, it seems like people go "You know what sounds like fun?!? Making a language.
# Mine will be more perfect than the rest because there are no drawbacks to any descision ever. Yeah."
# And then they go "That's too hard. Let's made an IDE. If that's too much then I'll strip out almost everything and market it like the new Vim."
# And so here we are.

# Back to lambdas. Which I feel like I finally understand.
# It's remarkable how complicated people can make things sound when the idea is unremarkable simple.

def overused(n):
    return lambda x: x - n
def lets_print_things(n):
    print(n)

you_must_go_back = overused(100)
lets_print_things(you_must_go_back(0))
# lets_print_things(overused(0))
# nope

# lets me define the function of functions, mother of dragons but does not let me call on little drogo.
# drogo = khaleesi(you_must_go_back(100))
# drogo(1)

lets_print_things(you_must_go_back(0)) # should be '-100'
lets_print_things(you_must_go_back(1)) # should be '-101'
lets_print_things(you_must_go_back(0)) # should be '-101'

# weird shit, got -100, -99, -100. From fn assignment?
print(you_must_go_back(100)) # got 0.
# print(overused(10)) # returns error
# print(overused(1)) # returns error
