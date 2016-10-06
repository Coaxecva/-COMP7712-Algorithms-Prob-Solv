
votes = [ 'c', 't', 's', 'j', 'c', 'c', 't', 'c', 't', 'c' ]
# an element is a majority if it occurs more than half of the time.

def maj(L):
	for x in L:
		count = 0
		for y in L:
			if x == y:
				count += 1
		if count > len(L)//2:
			return x
	return None