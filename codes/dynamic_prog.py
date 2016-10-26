# dynamic programming
Table = {}
def fib(n):
	if n not in Table:
		if n<2:
			Table[n] = n
		else:
			Table[n] = fib(n-1) + fib(n-2)
	return Table[n]

def fib_i(n):
	if n < 2:
		return n
	F = [0] * (n+1)
	# Want: F[i] == fib(i)
	F[0], F[1] = 0, 1
	for i in range(2, n+1):
		F[i] = F[i-1] + F[i-2]
	return F[n]

for i in range(100):
	print(i, fib(i), fib_i(i))