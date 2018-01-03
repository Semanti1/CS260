#!/usr/bin/python3

from heap import *

def main():
	L=heap();
	print("Welcome to heap");
	print("The List of Commands is below, type help to see them again.")
	print("help - Prints this list")
	print("makenull - Clears the heap")
	print("insert <integer> - Inserts the number into the heap")
	print("min - Prints the current min on the heap")
	print("inorder - Prints heap in inorder")
	print("preorder - Prints heap in preorder")
	print("postorder - Prints heap in postorder")
	print("deletemin - Removes min from the heap")
	print("sort - Calls deletemin repeatedly to print out sorted numbers")
	print("exit - Exits the program (also Crtl-D exits)")
	command=input(">")
	c=command.split(' ',1)
	while c[0]!='exit':
		if c[0]=="help":
			print("help - Prints this list")
			print("makenull - Clears the heap")
			print("insert <integer> - Inserts the number into the heap")
			print("min - Prints the current min on the heap")
			print("inorder - Prints heap in inorder")
			print("preorder - Prints heap in preorder")
			print("postorder - Prints heap in postorder")
			print("deletemin - Removes min from the heap")
			print("sort - Calls deletemin repeatedly to print out sorted numbers")
			print("exit - Exits the program (also Crtl-D exits)")
		elif c[0]=="makenull":
			L.makenull();
		elif c[0]=="insert":
			num=int(c[1])
			L.insert(num)
		elif c[0]=='min':
			print(L.min())
		elif c[0]=="inorder":
			print(L.inorder(0))
		elif c[0]=="preorder":
			print(L.preorder(0))
		elif c[0]=="postorder":
			print(L.postorder(0))
		elif c[0]=="deletemin":
			L.deletemin()
		elif c[0]=="sort":
			j=0
			k=len(L.data)
			while j<k:
				print(L.min())
				L.deletemin()
				j=j+1
		else:
			print('bad command');
		command=input(">");
		c=command.split(' ',1)


if __name__=="__main__":
        main()
	
