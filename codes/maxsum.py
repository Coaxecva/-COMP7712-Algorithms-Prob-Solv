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

def left_sum(L, left, right):
	ms, cur_sum = L[right], 0
	for i in range(right,left-1,-1):
		cur_sum += L[i]
		if cur_sum > ms:
			ms = cur_sum
	return ms

def right_sum(L, left, right):
	ms, cur_sum = L[left], 0
	for i in range(left, right+1):
		cur_sum += L[i]
		if cur_sum > ms:
			ms = cur_sum
	return ms

def max_sum(L):
	if len(L) == 1
		return L[0]
	# compute max sums of two halves
	# compute max sum of overlapping interval
	# return the correct value

prices = [10,-20,5,15,0,-10,15,-20,7,15]

# print( brute_force(prices) )