def isFibo(n):
	"""Return True if given positive integer n is Fibonacci num else False"""
	a, b = 1, 1
	while True:
		a, b = b, a+b
		if a == n:
			return True
		elif a > n:
			return False

def fibolist(n, end=False):
	"""Return n-length list of Fibonacci numbers as default
	Return list of Fibonacci numbers up to n if end is True
	"""
	a, b = 1, 1
	fiblist = [a]
	if end:
		while a < n:
			fiblist.append(a)
			a, b = b, a + b
	else:
		for i in range(n-1):
		    a, b = b, a + b
		    fiblist.append(a)
	return fiblist

def nthfibo(n):
	"""Return nth Fibonacci number"""
	return fibolist(n)[-1]
