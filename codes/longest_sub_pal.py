# longest palindromic subsequence
# x is a palindrome if x = reverse of x
Table = {}
seq = 'ACAGGTATTC'
# A, C, G, T, AA, AAA, ACA, GG, CAAC, CTTTC, CAGGAC

# pal(S,i,j) returns length of LPS of S[i:j+1].
def pal(S, i, j):
	if (i,j) not in Table:
		if i==j:
			Table[i,j] = 1
		elif i>j:
			Table[i,j] = 0
		elif S[i]==S[j]:
			Table[i,j] = 2 + pal(S,i+1,j-1)
		else:
			Table[i,j] = max(pal(S,i+1,j), pal(S,i,j-1))
	return Table[i,j]

def pal_i(S):
	t = {}
	# t[i,j] = Table[i,j] = pal(S,i,j)
	for i in range(len(S)):
		t[i,i] = 1
		t[i,i-1] = 0
	for i in range(len(S)-1,-1,-1):
		for j in range(i+1,len(S)):
			if S[i]==S[j]:
				t[i,j] = 2 + t[i+1,j-1]
			else:
				t[i,j] = max(t[i+1,j], t[i,j-1])
	return t[0,len(S)-1]

import util
seq = util.random_str(500, 'ACGT')
print(pal_i(seq))
print(pal(seq, 0, len(seq)-1))