from collections import defaultdict
import math
def sieve(start,end):
    primes = defaultdict(lambda: True)
    primes[1] = False
    for m in range(2,int(math.ceil(math.sqrt(end)))):
        initial_multiplier = max(int(math.ceil(start/m)),2)
        occurrence_in_interval = initial_multiplier*m
        while occurrence_in_interval <= end:
            primes[occurrence_in_interval] = False
            occurrence_in_interval += m

    return [x for x in range(start,end+1) if primes[x] is True]


if __name__ == '__main__':
    l,r = 1000,2000
    print(sieve(l,r))


