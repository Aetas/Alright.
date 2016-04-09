# this proves that 'continue' is indeed a thing languages should have
end = 10
for num in range(2,end):
    if num == (end - 1):
        print("End of the line bub. Take your ", num, " and go.")
        # continue # would break behave any differently?
        break # nope
    if num % 2 == 0: # white space, slayer of men.
        print("This numbah is divisible by 2!", num)
        continue # pass go, do not collect allowance
    print("Who cares about this number", num)
# does python have C/Rust print? That'd be nice.
