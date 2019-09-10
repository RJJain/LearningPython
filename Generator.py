#!/usr/bin/python2.7

import sys

def fibonacci(n):  # generator function
	a, b, counter = 0,1,0
	
	while True:
		if( counter > n ):
			return
		yield a
		a, b = b, a+b
		counter += 1
		
if __name__=='__main__':  # Allows us to run the Python file as reusable module or standalone program
	f = fibonacci( 5 )	# f is iterator object
	
	while True:
		try:
			print( next(f) )
		except StopIteration:
			sys.exit()
	
