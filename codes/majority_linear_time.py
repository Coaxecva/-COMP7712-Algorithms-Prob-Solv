
A = [1,1,0,1,1,0,2,1,1,1,0,0,1,0,1,2]

def majority(S):
	if len(S) == 0:
		return None
	elif len(S) == 1:
		return S[0]
	elif len(S) == 2:
		return S[0] if S[0]==S[1] else None
	if len(S)%2==1:
		count = len([y for y in S if y==S[-1]])
		if count > len(S)/2:
			return S[-1]
		S.pop()
	B = []
	for i in range(0,len(S),2):
		if S[i] == S[i+1]:
			B.append(S[i])
	m = majority(B)
	return m if len([y for y in S if y==m]) > len(S)/2 else None

	# B = [ S[i] for i in range(0,len(S),2) if S[i]==S[i+1] ]

print( majority([1,0,2,2]) )