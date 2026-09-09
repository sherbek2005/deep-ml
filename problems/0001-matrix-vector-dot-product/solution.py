def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	n  = len(a)
	m = len(a[0])
	k =len(b)
	if m != k: return -1

	res = [0]*n
	for i in range(0,k):
		for j in range(0,n):
			res[j] += b[i] * a[j][i]
	
	return res
