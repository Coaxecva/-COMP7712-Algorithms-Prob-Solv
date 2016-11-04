# matrix multiplication.
# A*B*C*D*E*F
# A*B
# Input: D (a list of matrix dimensions) D = [(3,5),(5,10),(10,2),(2,20),(20,100)]
# Output: find the min number of operations to multiply these matrices.

# Count(D, i, j) returns minimum number of operations to multiply M_i, M_i+1, ...., M_j
def Count(D, i, j):
	if i==j:
		return 0
	if i+1==j:
		A, B = D[i], D[i+1]
		return A[0] * A[1] * B[1]

	m = Count(D,i,i) + Count(D,i+1,j) + D[i][0]*D[i][1]*D[j][1]
	best_split = i
	for k in range(i,j):
		value = Count(D,i,k) + Count(D,k+1,j) + D[i][0]*D[k][1]*D[j][1]
		if value < m:
			m = value
			best_split = k
	print("%s, %s: (%s, %s), (%s, %s)" % (i,j, i,best_split,best_split+1,j))
	return m


D = [(3,5),(5,10),(10,2),(2,20),(20,100)]
print( Count(D, 0, len(D)-1) )