import sys
sys.setrecursionlimit(10**4)
def find_fib_pos(n):
    '''Takes a fibonacci number and returns
        the nth number of the fibonacci number'''

    x = 1000
    fib_nums = []
    a, b = 0, 1

    counter = 0

    while counter < x:
        a, b = b, a + b
        fib_nums.append(a)
        counter += 1

    fib_nums.pop(0)
    def findList(lst, ele):
        if not lst:         # base case: the list is empty
            return False
        elif lst[0] == ele: # check if current element is the one we're looking
            return True
        elif not isinstance(lst[0], list): # if current element is not a list
            return findList(lst[1:], ele)
        else:                              # if current element is a list
            return findList(lst[0], ele) or findList(lst[1:], ele)

    is_fib = findList(fib_nums, n)

    if is_fib:
        for i in range(len(fib_nums)):
            if n == fib_nums[i]:
                return i + 1
    else:
        return None