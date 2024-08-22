def first_deriv(x0, f):
    e = 0.0001
    return (f(x0 + e) - f(x0)) / e

def second_deriv(x0, f):
    e = 0.0001
    return (f(x0 + 2*e) - 2*f(x0 + e) + f(x0)) / (e**2)

def optimize(x0, f):
    eps = 2.22044604925e-16
    x1 = x0 - first_deriv(x0, f) / second_deriv(x0, f)
    while abs(x1 - x0) > eps:
        x0 = x1
        x1 = x0 - first_deriv(x0, f) / second_deriv(x0, f)
    return x1