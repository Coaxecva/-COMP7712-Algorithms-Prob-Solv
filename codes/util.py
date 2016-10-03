import random

def random_list(n, Min, Max):
	return [ random.randint(Min,Max) for i in range(n) ]


if __name__ == '__main__':
	for i in range(10):
		print(random_list(20,-100,100))