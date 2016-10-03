# Input: A and B are sorted lists
# Output: merged list of A and B
# Running time, input size = n = lengths of A and B.  Theta(n)
# T(n) = c + T(n-1) is in Theta(n)
# S(n) = c + S(n-1) is in Theta(n)
def M(A, B):
	if A == []:
		return B
	if B == []:
		return A
	if A[0] < B[0]:
		return [A[0]] + M(A[1:], B)
	else:
		return [B[0]] + M(A, B[1:])

# Input: an unsorted list of numbers
# Ouput: a sorted list of numbers in L 
# Running time: T(n) = n + 2*T(n/2), in Theta(n log n)
# Space complexity: S(n) = 1 + 2S(n/2), in Theta(n)
def Sort(L):		# S(n)
	if len(L) <= 1:
		return L
	mid = len(L)//2
	A = Sort(L[:mid])   
	B = Sort(L[mid:])
	return M(A, B)

def random_list(n):
	import random
	return [ random.randint(0,20) for x in range(n) ]

L = random_list(300)
print(L)
print(Sort(L))