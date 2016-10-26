
votes = [ 'c', 't', 's', 'j', 'c', 'c', 't', 'c', 't', 'c','c' ]
# an element is a majority if it occurs more than half of the time.

# Time: Theta(n^2)
# Space: Theta(1)
def brute_force(L):
	for x in L:
		count = 0
		for y in L:
			if x == y:
				count += 1
		if count > len(L)/2:
			return x
	return None

# Time: T(n) = c*n + 2*T(n/2).  So, T(n) is in Theta(n log n)
# Space: Theta(1)
def majority(V, L, R):
	if L==R:
		return V[L]
	mid = (L+R)//2
	m1 = majority(V, L, mid)
	m2 = majority(V, mid+1, R)
	if m1==m2:
		return m1
	count1, count2 = 0, 0
	for i in range(L,R+1):
		if V[i] == m1:
			count1 += 1
		if V[i] == m2:
			count2 += 1
	if count1 > (R-L+1)/2:
		return m1
	if count2 > (R-L+1)/2:
		return m2
	return None


import util
import time
for n in range(5000, 100000, 1000):
	votes = util.random_list(n, 0, 2)
	start = time.time()
	# brute_force(votes)
	majority(votes, 0, len(votes)-1)
	end = time.time()
	print(n, end-start)
