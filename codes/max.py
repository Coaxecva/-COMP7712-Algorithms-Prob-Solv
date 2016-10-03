
def MAX(L):
	if len(L) == 1:
		return L[0]
	m = MAX(L[1:len(L))]
	if m < L[0]:
		return L[0]
	return m

'''
MAX is correct when input size is 1. (lines 3-4)
Assume that MAX is correct for input size 1,2,...,k, and L has k+1 elements.
Say, L=[x_1,x_2,...,x_k+1].
Then, line 5, 
m = MAX( [x_2, x_3, ..., x_k+1] )
m is largest element among x_2, x_3, ..., x_k+1
lines 6-8:  m is the largest among x_1, x_2, ..., x_k+1.  Therefore, MAX is correct 
for input size k+1.

Therefore, MAX is correct for all input sizes (except input size 0).

GOAL: prove P is correct for all input sizes:
Induction has 2 steps:
(1) Prove P is correct for all smallest irreducible inputs.
(2) Prove: "If P is correct for input sizes 0, 1, 2, ..., k,
 			then P is also correct for input size k+1."  (for any k)


After carrying out these 2 steps, why is P correct for all inputs?
Is P correct for input size 0?  Yes, because (1)
Is P correct for input size 1?  Yes, 
	because in (2),"If P is correct for input size 0, it is correct for input size 1."
Is P correct for input size 2?  Yes
because in (2),"If P is correct for input size 0,1, then P is correct for input size 2."





'''