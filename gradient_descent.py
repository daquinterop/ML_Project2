import numpy as np

def gradient_descent(grad_f, x_init, eta):
    x = x_init
    while True:
        x = x - eta * grad_f(x)
        if  np.linalg.norm(grad_f(x)) < 1e-4:
            return x
