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

prices = [10,-20,5,15,0,-10,15,-20,7,15]
A = prices[0:len(prices)//2]
B = prices[len(prices)//2:len(prices)]
print(A, left_sum(A))
print(B, right_sum(B))
# print( brute_force(prices) )