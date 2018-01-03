import sys
import math
from heapq import *

def graph(filename):

	d=dict()
	#v1=[]
	#v2=[]
	#wt=[]
	#i=0
	with open(filename,'r') as f:
		numNodes=f.readline()
		for line in f:
			edge=line.split()
			v1=int(edge[0])
			v2=int(edge[1])
			wt=float(edge[2])
			d[v1,v2]=wt
	w, h = int(numNodes),int(numNodes);
	Matrix = [[0.0 for x in range(w)] for y in range(h)] 
	#print(Matrix)
	#print (d)
	for x in range(int(numNodes)):
		for y in range(int(numNodes)):
			if x!=y:
				key=x,y
				if key in d:
					Matrix[x][y]=d[key]
				else:
					Matrix[x][y]=float('inf')
	#for i in range(int(numNodes)):
	#	for j in range(int(numNodes)):
			#print('{0}  '.format(Matrix[i][j]))
			#sys.stdout.write(str(Matrix[i][j])+" ")
		#print("")
	#print(len(Matrix))
	return Matrix


def dijkstra(G,start_node):
	#s=set();
	#s.add(start_node);
	s=[]
	dist=dict()
	li=[]
	#li=[float('inf'),float('inf'), float('inf'),float('inf'), float('inf')]
	l=len(G)
	P=[]
	for i in range(l):
		li.append(float('inf'))	
	for x in range(l):
		if x!=start_node:
			dist[x]=float('inf')
			P.append('N')
		else:
			dist[x]=0.0
			P.append(start_node);
	Q=[]
	for x in range(l):
		heappush(Q,(dist[x],x))
	while Q:
		#u=heappop(Q)
		u=nsmallest(1,Q)
		#print(u)
		heappop(Q)
	#	s.add(u[0])
		s.append(u[0])
		#print(u)
		#li[u[0][1]]=u[0][0]	
		for j in range(l):
			if (G[u[0][1]][j]>0 and G[u[0][1]][j]!=float('inf')):
				w=float(G[u[0][1]][j])
				#print(w)
				if (dist[j]>(dist[u[0][1]]+w)):
					dist[j]=dist[u[0][1]]+w
					P[j]=u[0][1]
					heappush(Q,(dist[j],j))
	#return s
	i=0
	print (P)
	while i<len(s):
		a=s[i][0]
		b=s[i][1]
		if li[b]>a:
			li[b]=a
		i=i+1
	return li
		
def floyd(G): 
	num=len(G)
	w, h = num,num;
	P = [['N' for x in range(w)] for y in range(h)]
	for k in range(num):
		for i in range(num):
			for j in range(num):
				if G[i][k]+G[k][j]<G[i][j]:
					G[i][j]=G[i][k]+G[k][j]
					P[i][j]=k
	print(P)
	#for a in range(num):
	#	for b in range(num):
			
	return G;
					
					

def main():
	#G=graph('input1.txt')
#	s=set();
#	s.add('a');
#	s.add('a');
#	print(s)
	filename=input('File containing graph:')
	G=graph(filename)
	print("Possible Commands Are:")
	print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
	print("floyd - Runs Floyd's algorithm")
	print("help - prints this menu")
	print("exit or ctrl-D - Exits the program")
	command=input("Enter Command:")
	c=command.split(' ',1)
	while c[0]!='exit':
		if c[0]=='help':
			print("Possible Commands Are:")
			print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
			print("floyd - Runs Floyd's algorithm")
			print("help - prints this menu")
			print("exit or ctrl-D - Exits the program")
		elif c[0]=='floyd':
			A=floyd(G)
			for x in range(len(A)):
				print(A[x])
		else:
			print(dijkstra(G,int(c[1])))
		command=input('Enter Command:')
		c=command.split(' ',1)
	print('Bye')

	#A=floyd(G)
	#print('floyd')
	#print(floyd(G))
	#print('dijkstra')
	#print(dijkstra(G,0))
	#print(dijkstra(G,1))
	#print(dijkstra(G,2))
	#print(dijkstra(G,3))
	#print(dijkstra(G,4))


if __name__=="__main__":
        main()

