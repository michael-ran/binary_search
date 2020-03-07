#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    left = 0
    right = len(xs) - 1
    
    if not xs:
        return None
    if xs[0] > 0:
        return 0
    
    def recursive_search(left, right):
        mid = (left + right)//2
        if xs[mid] == 0:
            return mid + 1
        if left == right:
            if xs[mid] > 0:
                return mid
            else:
                return None
        elif xs[mid] > 0:
            return recursive_search(left, mid-1)
        elif xs[mid] < 0:
            return recursive_search(mid + 1, right)

    return recursive_search(left, right)

def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    if not xs:
        return 0

    left = 0 
    right = len(xs) - 1
    
    def greater_than(left, right):
        mid = (left + right)//2
        
        if xs[mid] == x:
            if mid == 0 or xs[mid-1] > x:
                return mid
            else:
                return greater_than(left, mid-1)
        elif left == right:
            return None
        elif xs[mid] > x:
            return greater_than(mid + 1, right)
        elif xs[mid] < x:
            return greater_than(left, mid - 1)

    def less_than(left, right):
        mid = (left + right)//2
        
        try:
            if xs[mid] == x:
                if x > xs[mid + 1] or (len(xs) - 1) == mid:
                    return mid  
                else:
                    return less_than(mid+1, right)
        except IndexError:
            return mid
        if left == right:
            return None
        elif xs[mid] > x:
            return less_than(mid + 1, right)
        elif xs[mid] < x:
            return less_than(left, mid - 1)
    greater = greater_than(left, right)
    less = less_than(left, right)

    if greater == None or less == None:
        return 0
    else:
        return (less - greater) + 1

def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''

    def rec_arg(lo, hi):

        if hi - lo < epsilon:
            return hi 

        m1 = lo + (hi-lo)/4
        m2 = hi - (hi-lo)/2

        if f(m1) < f(m2):
            return rec_arg(lo, m2)
        if f(m1) > f(m2):
            return rec_arg(m1, hi)

    return rec_arg(lo, hi)
