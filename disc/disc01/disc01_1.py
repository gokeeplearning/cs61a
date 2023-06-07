# Question 1.1
def wears_jacket(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False


"""
Question 1.2
The function so_slow(5) contains an infinite loop because x will never become less than or equal to 0, and the division by zero will never be reached.
Therefore, the square(so_slow(5)) line is not reached, either.
As a result, there won't be any output from the square function or the "here!" print statement.
"""


# Question 1.3
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True


