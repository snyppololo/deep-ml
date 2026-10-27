import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    """
    Perform linear regression using gradient descent.

    Args:
        X: Feature matrix of shape (m, n) where first column is all ones (for intercept)
        y: Target vector of shape (m,)
        alpha: Learning rate
        iterations: Number of gradient descent iterations
    
    Returns:
        Learned weights as a 1D array of shape (n,)
    """
    m, n = X.shape
    y = y.reshape(-1, 1)  # Ensure y is a column vector
    theta = np.zeros((n, 1))  # Initialize weights to zeros

    # Your code here: implement gradient descent
    for i in range(iterations):
        inner_matrix = (X @ theta) - y
        # cost = 1 / (2*m) * np.transpose(inner_matrix) @ inner_matrix
        gradient = 1 / m * np.transpose(X) @ (X @ theta - y)
        # now update
        theta = theta - alpha * gradient
    return theta.flatten()