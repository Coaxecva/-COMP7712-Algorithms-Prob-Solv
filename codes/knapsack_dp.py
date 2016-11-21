
W = [6,3,4,2]
C = [3000,1400,1600,900]
Capacity = 10

def Knapsack(W,C,Cap):
	
	# K(weights, calories, cap, i) computes optimal value for the first i items, given capacity cap.
	def K(weights, calories, cap, i):
		if (cap,i) in Table:
			return Table[(cap,i)]

		if i < 0 or cap <= 0:
			return 0
		not_taken = K(weights, calories, cap, i-1)
		if cap < weights[i]:
			Table[(cap,i)] = not_taken
			return Table[(cap,i)]
		taken = calories[i] + K(weights, calories, cap-weights[i], i-1)
		Table[(cap,i)] = max(not_taken, taken)
		return Table[(cap,i)]
	# 1. i is in opt solution, then opt value = calories[i] + K(weights, calories, cap-weights[i], i-1)
	# 2. i is not in opt solution, then opt value = K(weights, calories, cap, i-1)

	Table = {}
	return K(W,C,Cap,len(W)-1)

print( Knapsack(W,C,Capacity) )

'''
Why do we cache? prevent recomputation.
We have a long-running function f with input I and output O
Hash table H.
Store O into H[I]
'''