import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0]) != len(b):
		return -1
	
	num_cols = len(a[:][0])
	
	res = [0]*len(a[0])
	for i in range(len(a[0])):
		partial = 0
		for j in range(num_cols):
			partial = partial + a[i][j] * b[j]
		res[i] = partial
	return res