import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	# (X^T * X)^-1 * X^T * y
	X_t = np.transpose(X)
	theta_noround = np.linalg.inv(X_t @ X) @ X_t @ y
	theta = np.round(theta_noround, decimals=4)
	return theta