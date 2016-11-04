
# returns if S[0:i+1] is a sequence of valid words.
def Valid(S, D, i):
	if S[0:i+1] in D:
		return True
	
	for j in range(i):
		u, v = S[0:j+1], S[j+1:i+1]
		if v in D and Valid(S, D, j):
			return True
	return False

d = {'it', 'was', 'the', 'best', 'of', 'times'}
s = 'itwasthebestoftimes'
s = 'itwasthe'
# print(Valid(s, d, len(s)-1))
t = 'tobehave'
print(Valid(t, {'behave', 'tobe', 'have'}, len(t)-1))