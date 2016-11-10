def get_set(L):
	return [ i for i in range(len(L)) if L[i] ]

# sets(i) assumes that Config is set for indices 0, 1, ..., i
# it will generate all subsets of N numbers with this configuration.
def sets(i):
	if i==N-1:
		print(get_set(Config))
	else:
		Config[i+1] = True
		sets(i+1)
		Config[i+1] = False
		sets(i+1)

N = 4
Config = [None]*N
sets(-1)
