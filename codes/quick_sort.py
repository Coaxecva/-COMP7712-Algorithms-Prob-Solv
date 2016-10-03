def SORT(L):
	if len(L) <= 1:
		return L
	pivot = L[0]
	A = [ x for x in L[1:] if x <= pivot ]
	B = [ x for x in L[1:] if x > pivot ]
	return SORT(A) + [pivot] + SORT(B)

def Split(L, left, right):
	pivot = L[left]
	l, r = left+1, right
	while l <= r:
		if pivot <= L[l]:
			L[l], L[r] = L[r], L[l]
			r = r - 1
		else:
			l = l + 1
	L[left], L[l-1] = L[l-1], L[left]
	return l-1

def SORT2(L, left, right):
	if left < right:
		i = Split(L, left, right)
		SORT2(L, left, i-1)
		SORT2(L, i+1, right)
		

import util
L = util.random_list(20,0,50)
print(L)
SORT2(L, 0, len(L)-1)
print(L)

# (average case, assuming a good split) Time complexity:
# T(n) =  2n + 2T(n/2) is in Theta(n log n)
# Space complexity
# S(n) = n + 2S(n/2) is in Theta(n log n)
# S(n) = c + 2S(n/2) is in Theta(n)

