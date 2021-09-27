import math 
import numpy as np 


def perceptron_train(X,Y):
    # Initialize perceptron. Perceptron is a list. 0:D slice contains the weights. D-th element is the bias.
    parameters = np.zeros(X.shape[1] + 1)
    # Sample processing order
    N = X.shape[0]
    D = X.shape[1]
    order = np.arange(N)
    np.random.shuffle(order)
    while True:
        updates = []
        for sample, label in zip(X[order], Y[order]):
            b = parameters[-1]
            w = parameters[:-1]
            a = sum([w[k]*sample[k] + b for k in range(D)])
            update = label * a <= 0
            updates.append(update)
            if update: # Update
                w = w + label*sample
                b = b + label
            parameters = np.append(w, b)
        if any(updates): # If converged
            continue
        else:
            return parameters[:-1], parameters[-1]


def perceptron_test(X_test, Y_test, w, b):
    Y_pred = np.array([np.sign(sum(w * sample + b)) for sample in X_test])
    return np.mean([y_pred == y for y_pred, y in zip(Y_pred, Y_test)])


if __name__ == '__main__':
    from test_script import load_data
    X,Y = load_data("data_1.txt")
    w,b = perceptron_train(X,Y)
    test_acc = perceptron_test(X,Y,w,b)
    print("Perceptron:",test_acc)

    X,Y = load_data("data_2.txt")
    w,b = perceptron_train(X,Y)
    X,Y = load_data("data_1.txt")
    test_acc = perceptron_test(X,Y,w,b)
    print("Perceptron:",test_acc)