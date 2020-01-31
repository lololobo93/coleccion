#################################################################################

# Este programa resuelve la ecuación diferencial de segundo orden:
#                 a(x)*h''(x) + a'(x)*h'(x) = f(x),
# para ello se requieeren los puntos extremos x0 y xf, así como las 
# condiciones de frontera:
#            h(x0) = h0         y            h(xf) = hf.
# Además, es necesario introducir las funciones a(x), a'(x) y f(x).
# Aunque podría no ser necesario introducir a'(x), por cuestiones de 
# precisión es mejor introducir esta función.

#################################################################################

# Paqueterías a usar

import numpy as np
import matplotlib.pyplot as plt

def expr_to_fn(expr):
    """ Devuelve una funcion lambda `fn`, obtenida a partir del string `expr` """
    expr_total = "lambda x : " + expr
    fn = eval(expr_total)
    return fn

def finite_diff_solver(x0, xf, h0, hf, af, af1, f, N):
    """ Resuelve la ecuación diferencial usando el método de diferencias finitas
        y gráfica la salución usando pyplot
    """ 
    a = np.zeros(N+2)
    b = np.zeros(N+2)
    c = np.zeros(N+2)
    d = np.zeros(N+2)

    h = (xf - x0)/(N+1)
    x = x0 + h
    a[1] = 2
    b[1] = - 1 - (h/2)*(af1(x)/af(x))
    d[1] = - h**2 * (f(x)/af(x)) + (1 - (h/2) * (af1(x)/af(x))) * h0 

    for i in range(2, N):
        x = x0 + i*h
        a[i] = 2
        b[i] = - 1 - (h/2)*(af1(x)/af(x))
        c[i] = - 1 + (h/2)*(af1(x)/af(x))
        d[i] = - h**2 * (f(x)/af(x))

    x = xf - h
    a[N] = 2
    c[N] = - 1 + (h/2)*(af1(x)/af(x))
    d[N] = - h**2 * (f(x)/af(x)) + (1 + (h/2) * (af1(x)/af(x))) * hf

    l = np.zeros(N+2)
    u = np.zeros(N+2)
    z = np.zeros(N+2)
    w = np.zeros(N+2)

    l[1] = a[1]
    u[1] = b[1] / a[1]
    z[1] = d[1] / l[1]

    for i in range(2, N):
        l[i] = a[i] - c[i]*u[i-1]
        u[i] = b[i] / l[i]
        z[i] = (d[i] - c[i]*z[i-1])/l[i]

    l[N] = a[N] - c[N]*u[N-1]
    z[N] = (d[N] - c[N]*z[N-1])/l[N]

    w[0] = h0
    w[N+1] = hf
    w[N] = z[N]

    for i in range(N-1, 0, -1):
        w[i] = z[i] - u[i]*w[i+1]

    x_array = np.zeros(N+2)

    for i in range(0, N+2):
        x_array[i] = x0 + i*h

    return (x_array, w)

def main():
    """ Función main donde se piden los valores necesarios y se llama el 
        método de diferencias finitas
    """
    x0 = float(input("Introduzca x0: "))
    xf = float(input("Introduzca xf: "))
    h0 = float(input("Introduzca h(x0): "))
    hf = float(input("Introduzca h(xf): "))

    expr = input("Introduzca a(x): ")
    a = expr_to_fn(expr)

    expr = input("Introduzca a'(x): ")
    a1 = expr_to_fn(expr)

    expr = input("Introduzca f(x): ")
    f = expr_to_fn(expr)

    x, w = finite_diff_solver(x0, xf, h0, hf, a, a1, f, 20)

    plt.plot(x, w)
    plt.ylabel('h(x)')
    plt.xlabel('x')
    plt.show()

main()