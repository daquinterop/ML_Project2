# Perceptron
##  perceptron_train(X,Y)
    The perceptron object is represented by a 1D array. Having D features, the perceptron is a 1D array of D+1 size.
    The 0:D slice of the array contains the weights and the D-th element is the bias. Then, the perceptron is 
    represented as follows:
        Perceptron = [w_1, w_2, w_3, ... , w_D, b]
    To train the perceptron the function goes over the next steps:
        - Initialize the perceptron with zeros for the weights and the bias.
        - Stablish the order of the samples randomly.
        - Iterate over all samples until convergence
            * Calculate activation (a)
            * Update weights and bias if y_k*a <= 0
            * If there was any update, then go and do new epoch
            * If there was not an update, then return the weights and bias.

## perceptron_test(X_test, Y_test, w, b)
    This function simply returns the mean of the hits. A hit is calculated for all the samples as 1 if the perceptron 
    defined by w, b parameters predicts correctly the label, and as 0 if it fails to predict the label. The predicted
    label for any sample is the sign of the activation.
