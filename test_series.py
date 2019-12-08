from series import fibonacci, lucas, sum_series

# testing for the fibonacci series

def test_fib_zero():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_fib_one():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_fib_two():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected

def test_fib_three():
    expected = 2
    actual = fibonacci(3)
    assert actual == expected

def test_fib_four():
    expected = 3
    actual = fibonacci(4)
    assert actual == expected

def test_fib_five():
    expected = 5
    actual = fibonacci(5)
    assert actual == expected

def test_fib_six():
    expected = 8
    actual = fibonacci(6)
    assert actual == expected

# testing for the lucas series
def test_lucas_zero():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_lucas_one():
    expected = 1
    actual = lucas(1)
    assert actual == expected

def test_lucas_two():
    expected = 3
    actual = lucas(2)
    assert actual == expected

def test_lucas_three():
    expected = 4
    actual = lucas(3)
    assert actual == expected

def test_lucas_four():
    expected = 7
    actual = lucas(4)
    assert actual == expected

def test_lucas_five():
    expected = 11
    actual = lucas(5)
    assert actual == expected

def test_lucas_six():
    expected = 18
    actual = lucas(6)
    assert actual == expected

# testing for the sum series

def test_sum_fib_one():
    expected = 1
    actual = sum_series(1)
    assert actual == expected

def test_sum_fib_three():
    expected = 2
    actual = sum_series(3)
    assert actual == expected

def test_sum_fib_six():
    expected = 8
    actual = sum_series(6)
    assert actual == expected

def test_sum_lucas_one():
    expected = 1
    actual = sum_series(1, 2, 1)
    assert actual == expected

def test_sum_lucas_three():
    expected = 4
    actual = sum_series(3, 2, 1)
    assert actual == expected

def test_sum_lucas_six():
    expected = 18
    actual = sum_series(6, 2, 1)
    assert actual == expected
