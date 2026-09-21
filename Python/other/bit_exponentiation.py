def compute_power(base: int, exponent: int, mod: int = None) -> int:
    result = 1
    if exponent > 0:
        result = compute_power(base, exponent//2, mod)
        result = result * result if exponent % 2 == 0 else result * result * base
    return result if mod is None else result % mod

if __name__ == '__main__':
    MOD = 10**9+7
    print(compute_power(2,3, MOD))
    print(compute_power(2, 10, MOD))
    print(compute_power(10, 10, MOD))
    print(compute_power(5, 100, MOD))