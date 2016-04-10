# this seems like it could be quite handy. Not much obvious advantage over C+P overloading or just having a string argument but hey.

# can you assign via input in one line? I'll have to try.
# I also wonder if you could assign in a function call argument initialization. If that makes any sense.

rt = 4 # it's interesting that the addition of this assignment makes the rt variable pass into the method regardless of whether or not it is used.
# just kidding, it's global no matter what. At least for reading. 

def just_do_it(words, retries=rt, complain='Can I reassign this string at call?'):
    print('rt: ', rt, '\nretries: ', retries)
    while True:
        decision = input(words) # this just says what words contains and then grabs input ot assign to decision, yes?
        if decision in ('y','ye','yes'): # does this take care of caps? I'm going ot guess no but I could be wrong.
            return True
        if decision in ('n','no','nope','nadda','nopers'):
            return False # this breaks out of the function call in Python, right? It should...
        retries -= 1 # this works..? retries-- won't. I think. e: yes, it works
        if retries < 0:
            raise OSError('Criminal scum') # this is a kinda strange thing right here.
        print(complain)

just_do_it('Hey.')

just_do_it('Ahoy. ', 1) # allright, so it has no problem being reassigned despite being assigned.
# and if I don't initialize the number at default call then it will hold the same number.
# in fact, I'm sure it would bitch because it would keep the same running total for retries accross all calls.
# that's weird. Isn't it a terrible idea to keep an object around forever unless you kill it? RAII and that.
# and in a complicated function, Python will carry around your failures with you until it fails in the nth call from lack of re-initializzation.
# anywho.

just_do_it('Sup. ', 10, 'Boop.') # works as expected.

just_do_it('Don\'t do it. ', 'string decriment error?') # I'm guessing this should fail if anything but a True/False case is input...
# it indeed does.
