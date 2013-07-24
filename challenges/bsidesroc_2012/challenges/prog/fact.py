#!/usr/bin/python

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

result = sum(map(int,str(factorial(100))))

print 'Result is: %d' % result 
