A = [1,2,3,4,5,6]

def R(L):
	if len(L) == 0:
		return []
	else:
		return R(L[1:len(L)]) + [L[0]]

print( R(A) )
'''
Trace:
R([1,2,3,4,5,6]) -> R([2,3,4,5,6]) + [1] -> R([3,4,5,6])+[2]+[1]
-> R([4,5,6])+[3]+[2]+[1] -> R([5,6])+[4]+[3]+[2]+[1]
-> R([6]) + [5] + [4] + [3] + [2] + [1] 
-> R([]) + [6] + [5] + [4] + [3] + [2] + [1]
-> [] + [6] + [5] + [4] + [3] + [2] + [1] -> [6,5,4,3,2,1]


Mathematical induction:
(1) R is correct for input size 0.  (lines 4-5)
(2) Assume R is correct for input sizes 0, 1, ..., k. Let's say L has
k+1 items.  So, R(L) returns (line 7) R(L[1:len(L)]) + [L[0]].
This return value is: reverse of L[1:]  + [L[0]], which is the reverse of L.
Therefore, R is correct for all input sizes.

Mathematical induction on input [1,2,3,4,5,6]
R is correct for empty lists. This is the smallest case.
R([1,2,3,4,5,6]) returns R([2,3,4,5,6]) + [1], which is [6,5,4,3,2] + [1] 
(assuming that R returns correct values for input sizes less 6).  This is
[6,5,4,3,2,1], which is the correct answer.

'''