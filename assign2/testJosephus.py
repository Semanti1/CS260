from node import *
from queue import *
import sys

def test(N,M):
	Q=Queue()
	i=0
	while i<N:
		Q.enqueue(i)
		i=i+1
	Q1=Queue()
	Q2=Queue()
	#print(str(Q))
	i=1;
	while Q.empty()==False:
		if i%M!=0:
			Q1.enqueue(Q.front())
			Q.dequeue()
			#print(str(Q1))
		else:
			Q2.enqueue(Q.front())
			Q.dequeue()
		if Q.empty():
			Q=Q1
		i=i+1;
	while Q2.empty()==False:
		print(Q2.front(),end=" ")
		Q2.dequeue()
	print()
def main():

	N=int(sys.argv[1])
	M=int(sys.argv[2])
	test(N,M)
if __name__ == "__main__":
    main()

	
