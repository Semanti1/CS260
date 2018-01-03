#!/usr/bin/python3
import math

count=0
mem=dict()

def add(a,b):
	global count
	count=count+1
	return a+b

def fib_closed(n):
	fib=(math.pow((1+math.sqrt(5)),n) -math.pow((1-math.sqrt(5)),n ))/(math.pow(2,n)*math.sqrt(5))
	return int(fib)

def fib_classic(n):
	global count
	#count=0
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		fib=add(fib_classic(n-2),fib_classic(n-1))
		return fib

def fib_loop(n):
	global count
	count=0
	lcount=n-1
	a=0
	b=1
	c=0
	while lcount>0:
		c=add(a,b)
		a=b
		b=c
		lcount=lcount-1
	return c


def fib_mem(n):
	global mem
	global count
	if (n in mem):
		return mem[n]
	else:
		if n==0:
			mem[n]=0
			return mem[n]
		elif n==1:
			mem[n]=1
			return mem[n]
		else:
			mem[n]=add(fib_mem(n-2),fib_mem(n-1))
			return mem[n]

def main():
	global count
	count=0
	print('Welcome to the Fibonacci Test Program')
	print('To exit, enter a negative number.')
	num=int(input('Enter Fibonacci Number to compute:\n'))
	while num>= 0:
		print("--------------------\n")
		print ('Computing the {0}th Fibonacci Number:\n'.format(num))
		count=0
		print ("The closed form finds: ",fib_closed(num))
		print("The recursive definition finds: ",fib_classic(num))
		print("Additions needed for recursive definition : ",count)
		count=0
		print("The loop definition finds: ",fib_loop(num))	
		print("Additions needed for loop  definition : ",count)
		count=0
		print("The memoization definition finds: ",fib_mem(num))
		print("Additions needed for memoization definition : ",count)
		num=int(input('Enter Fibonacci Number to compute:\n'))

		
if __name__ == "__main__":
        main()

	

		


	

