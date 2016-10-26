# find the interval that gives the maximum sum.
# 22, 5+15+0-10+15-20+7+15=27

def brute_force(L):
	ms, interval = L[0], [0,0]
	for i in range(0, len(L)):
		sum_i2j = 0
		for j in range(i, len(L)):
			sum_i2j += L[j]
			if ms < sum_i2j:
				ms, interval = sum_i2j, [i,j]
	return ms, interval	

def left_sum(L):
	ms, cur_sum = L[len(L)-1], L[len(L)-1]
	for i in range(len(L)-2,-1,-1):
		cur_sum += L[i]
		if cur_sum > ms:
			ms = cur_sum
	return ms

def right_sum(L):
	ms, cur_sum = L[0], L[0]
	for i in range(1, len(L)):
		cur_sum += L[i]
		if cur_sum > ms:
			ms = cur_sum
	return ms

def max_sum(L):
	if len(L) == 1:
		return L[0]
	A, B = L[0:len(L)//2], L[len(L)//2:len(L)]
	return max( max_sum(A), max_sum(B), left_sum(A)+right_sum(B) )


Table = {}
# the max sum of an interval that MUST end at index i.
# we store opt(L,i) in Table[i]
def opt(L, i):
	if i not in Table:
		Table[i] = max(L[i], L[i] + opt(L,i-1)) if i>0 else L[0]
	return Table[i]

def opt_max_sum(L):
	return max([ opt(L,i) for i in range(len(L)) ])

# table[i] stores the max sum of an interval that MUST end at index i.
# this means table[i] == opt(L,i)
def opt_max_sum_i(L):
	table = [0] * len(L)
	table[0] = L[0]
	for i in range(1, len(L)):
		table[i] = max(L[i], L[i]+table[i-1])
	return max(table)

# print( opt_max_sum([-10,20,30,-35,70]))
import util
import time
for n in range(500000, 2000000, 100000):
	prices = util.random_list(n, -100, 100)
	print(n)
	# start = time.time()
	# brute_force(prices)
	# print("brute force", time.time() - start)
	start = time.time()
	max_sum(prices)
	print("dnc", time.time() - start)
	start = time.time()
	opt_max_sum(prices)
	print("opt", time.time() - start, len(Table))
	Table = {}
	start = time.time()
	opt_max_sum_i(prices)
	print("opt_i", time.time() - start)

