A = [1,1,0,1,1,0,2,1,1,1,0,0,1,0,1,2]

#problem1 

def majority(S):
	if len(S) == 0:
		return None
	elif len(S) == 1:
		return S[0]
	elif len(S) == 2:
		return S[0] if S[0] == S[1] else None
	if len(S) % 2 ==1:
		count = len([y for y in S if y == S[-1]])
		if count > len(S)/2:
			return S[-1]
		S.pop()	
	B = []
	for i in range(0, len(S), 2):
		print(S,i)
		if S[i] == S[i+1]:
			B.append(S[i])
	m = majority(B)
	return m if len([y for y in S if y == m ]) > len(S)/2 else None	



# print(majority(A))

#problem 3
def Valid(S,D,i):
	if S[0:i+1] in D:
		return True
	for j in range(i):
		u, v = S[0:j+1], S[j+1:i+1]
		if v in D and Valid(S,D,j):
			return True
	return False


d = {'it', 'was', 'the', 'best', 'of', 'times'}
s =  'itwasthebestoftimes'
print(Valid(s,d,len(s)-1))