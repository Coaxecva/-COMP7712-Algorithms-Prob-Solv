##------------------------------------------------------------------
def Search(L, x, left, right):
	if left > right:
		return False
	mid = (left+right)//2
	if x == L[mid]:
		return True
	if x < L[mid]:
		return Search(L, x, left, mid-1)
	else:
		return Search(L, x, mid+1, right)

print(Search([1,2,3,4,5,7,90], 7, 0, 5))
'''
Let T(n) be the running of Search for input size n.
T(1) = c
T(n) = c + T(n/2) = 2c + T(n/2^2) = 3c + T(n/2^3)
T(n) = k*c + T(n/2^k) = log_2(n)*c + T(1) = log_2(n)*c + c, is in Theta(log n)
If n/2^k = 1, k = log_2(n)


T(n/2^2) = c + T(n/2^3)
'''

##------------------------------------------------------------------

# def f(L):
# 	if len(L) <= 1:
# 		return 1
# 	return 1 + f(L[1:len(L)])

'''
Define T(n) to be the running time of f for input size n.
T(n) = c + T(n-1) = c + (c + T(n-2)) = 2c + T(n-2) = 3c + T(n-3)
After k steps, T(n) = kc + T(n-k) = nc + T(0) = nc + 1
f stops when L has 0 items.  In other words n-k=0, or n=k.
T(0) = 1

T(n) = n*c + 1 is in Theta(n)
'''

##------------------------------------------------------------------
def g(L):
	if len(L) <= 1:
		return 1
	return 1 + g(L[0:len(L)//2])
'''
Define T(n) to be the running time of g for input size n.
T(n) = c + T(n/2) = 2c + T(n/2^2) = 3c + T(n/2^3)
After k steps, T(n) = kc + T(n/2^k)
g stops when n/2^k = 1, k = log_2(n).  T(1) = 1.
T(n) = log_2(n) * c + 1 is in Theta(log(n))

'''
##------------------------------------------------------------------
def h(L):
	if len(L) <= 1:
		return 1
	a = h(L[0:len(L)//2])
	b = h(L[1:len(L)])
	return a + b
'''
Define T(n) to be the running time of h for input size n.
T(n) = c + T(n/2) + T(n-1)
'''
##------------------------------------------------------------------
def f(L):
	n = len(L)
	i = 1
	sum = 0
	while i <= n:
		for j in range(n):
			sum += (i*j)
		i = i * 2

'''
step 0, i=1
step 1, i=2
step 2, i=2^2
...
step k, i=2^k
If loop exits after k steps, then 2^k = n.   k = log_2 n
log_2 n * n
'''