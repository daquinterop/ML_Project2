# Perceptron
##  perceptron_train(X,Y)
    The perceptron object is represented by a 1D array. Having D features, the perceptron is a 1D array of D+1 size. The 0:D slice of the array contains the weights and the D-th element is the bias. Then, the perceptron is represented as follows:
        Perceptron = [w_1, w_2, w_3, ... , w_D, b]
    The function goes over the next steps so as to train the perceptron:
        - Initialize the perceptron with zeros for the weights and the bias.
        - Stablish the order of the samples randomly.
        - Iterate over all samples until convergence
          E  |>>Call the current weights and bias         ˥
          P  |>>Calculate activation (a)                  |> Do this over all the samples
          O  |>>Update weights and bias if y_k*a <= 0     ˩
          C  |If there was any update during the epoch, then go to a new epoch.
          H  |If there was not an update, then return the weights and bias.
    The function will keep runing until there are updates. An max_epochs argument can be implemented so as to prevent the function to keep runing in an infite loop.

## perceptron_test(X_test, Y_test, w, b)
    This function simply returns the mean of the hits. A hit is calculated for all the samples as 1 if the perceptron defined by w, b parameters predicts correctly the label, and as 0 if it fails to predict the label. The predicted label for any sample is the sign of the activation of the perceptron.

# Gradient Descent
## gradient_descent(grad_f, x_init, eta)
    This function takes a gradient function, initial x vector and eta as input. The gradient descent is implemented through a While loop. Every interation the value of x is updated. That loop will keep runing until the magnitud of the gradient for the actual x value is below a threshold very near to cero. The function will return the x value when the magnitud of the gradient is near to cero.