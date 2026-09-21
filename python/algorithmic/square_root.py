"""
Create custom square root function using Newton-Raphson.
f(x_{n+1})  = f^{(0)}(x_n)(x_{n+1}-x_n)^0/0! + f^{(1)}(x_n)(x_{n+1}-x_n)/1!
            = f(x_n) + f^{(1)}(x_n)(x_{n+1}-x_n)
f(x_{n+1}) = 0 =>
                       0 = f(x_n) + f^{(1)}(x_n)(x_{n+1}-x_n)
                 -f(x_n) = f^{(1)}(x_n)(x_{n+1}-x_n)
    -f(x_n)/f^{(1)}(x_n) = (x_{n+1}-x_n)
 x_n-f(x_n)/f^{(1)}(x_n) = x_{n+1}

Here f(x) = x^2 - val.
"""
def sqrt(val, eps=10**(-5)):
    f0 = lambda x: x**2 - val
    f1 = lambda x: 2*x

    if val < 0:
        raise ValueError('Value must be non-negative!')
    elif val == 0:
        return 0
    else:
        x = val
        error = abs(f0(x))
        while error > eps:
            x -= f0(x)/f1(x)
            error = abs(f0(x))

    return x


if __name__ == '__main__':
    print(sqrt(4))
    print(sqrt(0))
    print(sqrt(100))
    print(sqrt(10))
    print(sqrt(101230))
