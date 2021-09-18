make_fib = lambda n: 1 if n <= 1 else make_fib(n - 1) + make_fib(n - 2)
#function above returns the nth fibonacci number

def gen_fib():
    '''Represents an infinte stream of fibonacci numbers'''
    i = 1
    while True:
        yield make_fib(i)
        i += 1

a = gen_fib() #creates an iterator

def nth_fib(n):
    '''Returns the nth position of a fibonacci number'''
    i = 1
    while True:
        if n == next(a):
            return i
        i += 1