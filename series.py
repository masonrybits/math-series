# returns the nth value in the fibonacci series in recursive

def fibonacci(n):
    if n < 0:
        print('incorrect input')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# returns the nth value in the lucas series in recursive

def lucas(n):
    if n < 0:
        print('incorrect input')
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

# returns the nth value in the sum series in recursive

def sum_series(n, a=0, b=1):
    if n < 0:
        print('incorrect input')
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        return sum_series(n-1, a, b) + sum_series(n-2, a, b)
