# this proves that 'continue' is indeed a thing languages should have
for num in range(2,10):
    if num % 2 == 0: # white space, slayer of men.
        print("This numbah is divisible by 2!", num)
        continue # pass go, do not collect allowance
    print("Who cares about this number", num)
# does python have C/Rust print? That'd be nice.
