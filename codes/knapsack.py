'''
item		weight				calories			cal/wt
0				6					3000				500
1				3					1400				467
2				4					1600				400
3				2					900					450

Cap = 10
{0, 2}
[ True, False, True, False ]
'''

def get_set(L):
	return [ i for i in range(len(L)) if L[i] ]

def total(sol, L):
	return sum( L[i] for i in sol)

def Knapsack(cap, weight, calories, i, cur_weight):
	global best, best_weight
	if i==N-1:
		s = get_set(Config)
		if cur_weight <= cap and (best==None or total(s, calories)>total(best, calories)):
			best = s
	else:
		Config[i+1] = True
		Knapsack(cap, weight, calories, i+1, cur_weight+weight[i+1])
		Config[i+1] = False
		Knapsack(cap, weight, calories, i+1, cur_weight)


def Knapsack2(cap, weight, calories, i, cur_weight, cur_cal):
	global best, best_weight, best_cal
	if promising(i, cur_weight, cap):
		if i==N-1:
			s = get_set(Config)
			if best==None or total(s, calories)>best_cal:
				best, best_cal = s, cur_cal
		else:
			Config[i+1] = True
			Knapsack2(cap, weight, calories, i+1, cur_weight+weight[i+1], cur_cal+calories[i+1])
			Config[i+1] = False
			Knapsack2(cap, weight, calories, i+1, cur_weight, cur_cal)


def promising(i, cur_weight, cap):
	if cur_weight > cap:
		return False
	return True

# W = [6,3,4,2]
# C = [3000,1400,1600,900]

import util
import time
best, best_weight = None, 0

for N in range(15,25):
	W = util.random_list(N, 10, 20)
	C = util.random_list(N, 2000, 3000)
	Cap = W[0] * len(W) * 0.4

	start_time = time.time()
	Config = [None]*N
	best, best_weight = None, 0
	Knapsack(Cap, W, C, -1, 0)
	end_time = time.time()
	print(N,end_time-start_time, best, Cap, total(best, W), total(best, C))

	start_time = time.time()
	Config = [None]*N
	best, best_weight = None, 0
	Knapsack2(Cap, W, C, -1, 0, 0)
	end_time = time.time()
	print(N,end_time-start_time, best, Cap, total(best, W), total(best, C))
