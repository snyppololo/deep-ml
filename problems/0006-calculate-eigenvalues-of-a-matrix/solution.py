import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	#formula is det(A-lambda*I) = 0
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	# (a-lambda) * (d-lambda) - bc = 0
	# ad - lambda*a - lambda*d + lambda^2 - bc = 0
	# lambda^2 - lambda(a+d) + ad - bc = 0
	coefficients = [1, -(a+d), a*d - b*c]
	eigenvalues = np.roots(coefficients)
	return eigenvalues.tolist()