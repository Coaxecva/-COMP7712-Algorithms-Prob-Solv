import time

# Theta(n^2)
def f(n):
	s = 0
	for i in range(n):
		for j in range(n):
			s = i*j + i+j
	return s

# Theta(n^2)
def g(n):
	s = 0
	for i in range(n):
		for j in range(i,n):
			s = j*i*i
	return s

# Theta(n log n)
def h(n):
	s = 0
	i = 1
	while i < n:
		for j in range(n):
			s = i*j
		i = i*10
	return s

# Theta(n)
def x(n):
	s = 0
	for j in range(n):
		i = 1
		while i < n:
			i = i + n/10
			s = i*j + i
	return s


# T(n) = 0.5*n + T(n/2).  So, T(n) is in Theta(n)
# say L has n items
# S(n) is in Theta(n)
def A(L)
	if len(L) <= 1:
		return 10
	m = L[0:len(L)//2]
	return 10 + A(m)


# S(n) is in Theta(n)
def B(L):
	if len(L) <= 1:
		return 1
	s = 0
	for i in range(len(L)):
		for j in range(i, len(L)):
			s = i*j
	return 10 + B([0:len(L)//2])

# T(n) = n^2 + T(n/2). T(n) is in Theta(n^2)

