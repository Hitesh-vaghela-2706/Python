# Iterative Function to calculate (p^q)%n in O(log q)
def modulo(p, q, n):
	res = 1
	while (q > 0):
		if ((q & 1) != 0):
			res = res * p
		q = q >> 1 # q = q/2
		p = p * p # Change p to p^2
	return res % n
p = 2
q = 3
n = 5
print("modulo is ", modulo(p, q, n))
