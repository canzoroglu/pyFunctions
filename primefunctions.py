def isPrime(n):
	"""Returns True if given positive integer is prime number else False"""
	upto = n//2
	for i in range(2,upto):
		if n%i == 0:
			return False
	return True

def primeNums(num):
	"""Returns list of prime numbers up to given positive integer"""
	primeList = []
	for x in range(2, num):
		if isPrime(x):
			primeList.append(x)
	return primeList

def primeFactors(n):
	"""Returns dictionary of prime number factors of given positive integer
	where keys are the prime number factors and values are number of their occurrences
	"""
	factors = {}
	if isPrime(n):
		return n
	while n > 1:
		for i in range(2,n+1):
			if isPrime(i) and n%i == 0:
				n = n//i
				if i in factors:
					factors[i] += 1
				else:
					factors[i] = 1
				break
	return factors
