'''
n-Queen
'''

# perm(i) assumes that config is set for entries/levels 0, 1, 2, ..., i
# it will generates all permutations with this partial configuration.
def perm(i):
	if i==N-1:
		print(Config)
	else:
		for j in range(N):
			if j not in Config[0:i+1]:
				Config[i+1] = j
				perm(i+1)

def queen(i):
	if promising(i):
		if i==N-1:
			print(Config)
		else:
			for j in range(N):
				if j not in Config[0:i+1]:
					Config[i+1] = j
					queen(i+1)

def promising(i):
	for k in range(i):
		if i-k == abs(Config[i]-Config[k]):
			return False
	return True

N=5
Config = [None]*N
queen(-1)