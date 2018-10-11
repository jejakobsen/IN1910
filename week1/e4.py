"""
Write a function factorize that takes in an integer $n$, and 
returns the prime-factorization of that number as a list. 
For example factorize(18) should return [2, 3, 3] and factorize(23) 
should return [23], because 23 is a prime. Test your function by factorizing a 6-digit number.
"""
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def factorize(n):
	P = get_primes(n)
	ls = []
	while n > 1:
		for p in P:			
			if n%p == 0:
				ls.append(p)
				n = n/p
				break
	return ls	

print(factorize(921909))

"""
C:\\Users\\jensj\\OneDrive\\Skrivebord\\IN1910\\week1>python e4.py
[3, 23, 31, 431]
"""