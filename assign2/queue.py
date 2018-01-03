#!/usr/bin/python3

from node import *

class Queue:
	def __init__(self):
        	self.start = None
	def __str__(self):
		current = self.start
		if current==None:
			return "Queue Empty"
		result=""
		while current != None:
			result=result+str(current)
			current = current.getNext()
		#result=result+"None"
		if result=="None":
			return "Queue Empty"
		else:
			return result
	def front(self):
		if self.start==None:
			return None
		else:
			return self.start.getValue()
	def empty(self):
		if self.start == None:
			return True
		else:
			return False
	def enqueue(self,x):
		current = self.start
		if current==None:
			self.start=Node(x,None);
		else:
			while current.getNext()!=None:
				current=current.getNext()
			new_node=Node(x,None)
			current.setNext(new_node)
	def dequeue(self):
		current = self.start
		if current==None:
            		return
		new_start=current.getNext()
		self.start=new_start 
