x = 'thecatruns'
y = 'acatran'

def LCS1(x,y):
	opt = 0
	for i in range(len(x)):
		for j in range(i, len(x)):
			if x[i:j+1] in y and len(x[1:j+1]) > opt:
				opt = len(x[i:j +1])
				print(x[i:j+1])
	return opt		

# print(LCS(x,y))	

# def LCS2(x,y,i,j):
# 	if i < 0 and j < 0:
# 		return 0
# 	if x[i] != y[j]:
# 		return 0
# 	else:
# 		return 1 + LCS2(x,y,i-1,j-1)	

# dynamic
table={}
def LCS2(x,y,i,j):
	if(i,j) in table:
		return table[(i, j)]
	if i < 0 and j < 0:
		return 0
	if x[i] != y[j]:
		return 0
	else:
		table[(i, j)] = 1 + LCS2(x,y,i-1,j-1)
		return table[(i, j)]


# print(LCS2(x,y,len(x),len(y)))

def LCS(x,y):
	opt = 0
	for i in range(len(x)):
		for j in range(len(y)):
			opt = max(opt, LCS2(x,y,i,j))
	return opt

def LCSiter(x,y): 
	opt = 0 
	t = {}
	for i in range(len(x)):
		for j in range(len(y)):
			if x[i] != y[j]:
				t[(i,j)] = 0
			elif i == 0 or j == 0:
				t[(i,j)] = 1
			else:
				t[(i,j)] = 1 + t[(i-1, j-1)]
			opt = max(opt, t[(i,j)])
	return opt
#  length of longest common subsequence between x[0:i+1] and y[0:j+1]
# todo cache the value (i,j)
def lcs(x,y):
	Table = {}
	def lcsub(x,y,i,j):
		if (i,j) in Table:
			return Table[i,j]
		if i < 0 or j < 0:
			return 0
		if x[i] == y[j]:
			Table[i,j] = 1 + lcsub(x,y,i-1,j-1)
			return Table[i,j]
		else:
			Table[i,j] = max(lcsub(x,y,i-1,j), lcsub(x,y,i,j-1))
			return Table[i,j]
	Table = {}
	return lcsub(x,y,len(x)-1,len(y)-1)		

# print(lcsub(x,y,len(x)-1, len(y)-1))											
print(lcs(x,y))			