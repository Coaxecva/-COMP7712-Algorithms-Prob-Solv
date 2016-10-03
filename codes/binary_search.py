def search(x,L,left,right):
	if left > right:
		return False
	mid = (left+right)//2
	if x == L[mid]:
		return True
	if x < L[mid]:
		return search(x, L, left, mid-1)
	else:
		return search(x, L, mid+1, right)

def isearch(x, L):
	left, right = 0, len(L)-1
	while left <= right:
		mid = (left+right)//2
		if x == L[mid]:
			return True
		if x < L[mid]:
			right = mid-1
		else:
			left = mid+1
	return False

A = [1,3,5,7,9,11,13,15,17,211]
print( isearch(20,A) )
'''
input size = number of items between left and right.
logic is the same as in recursive algorithm.
Is isearch correct for smallest size? Yes. Line 22.

'''
