#!/usr/bin/env python3
import math



class heap:
	def __init__(self):
		self.data=[]
	def __str__(self):
		#print (self.data)
		arr=""
		i=0;
		while i<len(self.data):
			arr=arr+" "+str(self.data[i])
			i=i+1
		return arr
	def makenull(self):
		self.data=[]
#	def insert(self,x):
	#	self.data.append(x)
	#	i=len(self.data)-1
	#	upheap(i)
	def parent(self,i):
		p=math.floor((i-1)/2)
		return p
	def left(self,i):
		l=(i+1)*2-1
		return math.floor(l)
	def right(self,i):
		r=(i+1)*2
		return math.floor(r)
	def swap(self,a,b):
		#if ((a<0) or (b<0)):
		#	return
		if ((a<len(self.data))and (b<len(self.data))):
			temp=self.data[a]
			self.data[a]=self.data[b]
			self.data[b]=temp
		#else:
		#	return
	def upheap(self,i):
		if self.parent(i)<0:
			return
		elif self.data[self.parent(i)]<self.data[i]:
			return
		else:
			self.swap(i,self.parent(i))
			self.upheap(self.parent(i))
	def insert(self,x):
		self.data.append(x)
		i=len(self.data)-1
		self.upheap(i)
	def downheap(self,i):
		if ((self.left(i)>=len(self.data)) and (self.right(i)>=len(self.data))):
			return
		elif self.left(i)>=len(self.data):
			sc=self.data[self.right(i)]
			ind=self.right(i)
		elif self.right(i)>=len(self.data):
			sc=self.data[self.left(i)]
			ind=self.left(i)
		else:
			lc=self.data[self.left(i)]
			rc=self.data[self.right(i)]
			if lc<rc:
				sc=lc
				ind=self.left(i)
			else:
				sc=rc
				ind=self.right(i)
		if self.data[i]>sc:
			self.swap(i,ind)
			self.downheap(ind)
		else:
			return
	def inorder(self,i):
		res=""
		if (i<0):
			return res
		elif (i>=len(self.data)):
			return res
		
		else:
			res=res+self.inorder(self.left(i))
			res=res+" "+str(self.data[i])
			res=res+self.inorder(self.right(i))
			return res

	def preorder(self,i):
		res=""
		if (i<0):
			return res
		elif (i>=len(self.data)):
			return res
		else:
			res=res+" "+str(self.data[i])
			res=res+self.preorder(self.left(i))
			res=res+self.preorder(self.right(i))
			return res

	def postorder(self,i):
		res=""
		if (i<0):
			return res
		elif (i>=len(self.data)):
			return res
		else:
			res=res+self.postorder(self.left(i))
			res=res+self.postorder(self.right(i))
			res=res+" "+str(self.data[i])
			return res
	def min(self):
		if (len(self.data)):
			return self.data[0]
	#	return

	def deletemin(self):
		if len(self.data)>0:

			self.swap(0,len(self.data)-1)
			#if len(self.data)>0:
			self.data.pop()
			self.downheap(0)

#if __name__=="__main__":
def main():
	toins=[95,36,11,92,88,57,53,21,35,86]
	L=heap()
	i=0
	while i<len(toins):
		L.insert(toins[i])
		i=i+1
	#print(L)
	#print(str(L))
	print(L.inorder(0))
	print(L.preorder(0))
	print(L.postorder(0))
	j=0
	while j<len(toins):
		print(L.min())
		L.deletemin()
		j=j+1
if __name__=="__main__":
	main()		
			


