"""
Based on https://www.geeksforgeeks.org/n-th-number-whose-sum-of-digits-is-ten/
Consider a number to be magic if the sum of its digits equals 10.
"""
import math


def nth(n):

    skipped = 0
    print(19, skipped)

    for i in range(2, n):
        potential = 19 + (i-1) * 9
        sum, running = 0, potential
        while running > 0:
            sum += running % 10
            running //= 10
        if sum == 10:
            print(potential, skipped)
        else:
            skipped += 1

    """
    val = 19 + (n-1) * 9
    val += (int(math.log10(val)//1) - 1) * 9
    return val
    """


if __name__ == '__main__':
    nth(100)


    """
    print(nth(1))
    print(nth(2))
    print(nth(5))
    print(nth(10))
    print(nth(20))
    print(nth(50))
    """