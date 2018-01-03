#!/usr/bin/python3
import math

comp=0
def bubblesort(A):
	n=len(A)
	swapped=True
	comp=0
	while swapped:
		swapped=False
		for i in range(1,n):
			if A[i-1]>A[i]:
				temp=A[i-1]
				A[i-1]=A[i]
				A[i]=temp
				swapped=True
		comp=comp+i
	#for j in range(0,n):
	#	print(A[j])
	approx=math.ceil(math.log(math.factorial(len(A)),2))		
	print("Using bubble sort:")
	print( A)
	print("Comparisons: ",comp)
	print("Approx Min: ",approx)

def insertion(A):
	n=len(A)
	comp=0        
        #comp=0
	for i in range(1,n):
		j=i
		#print (A)
		#comp=comp+1
		while j>0 and A[j-1]>A[j]:
			temp=A[j-1]
			A[j-1]=A[j]
			A[j]=temp
			j=j-1
			comp=comp+1
		if j!=0:
			comp=comp+1
	print("Using insertion sort: ")
	print(A)
	print("Comparisons: ",comp)
	approx=math.ceil(math.log(math.factorial(len(A)),2))
	print("Approx-min: ",approx)

def mergesort(A):
	global comp
	mergeSort(A)
	print("Using mergesort: ")
	print(A)
	print("Comparisons: ",comp)
	approx=math.ceil(math.log(math.factorial(len(A)),2))
	print("Approx-min: ",approx)

def msort(A,start,stop):
	if start<stop:
		#return 
		middle=start+math.floor((stop-start)/2)
		msort(A,start,middle)
		print(A)
		msort(A,middle+1,stop)
		print(A)
		merge(A,start,middle,stop)
	else:
		return A

def merge(A,start,middle,stop):
	i=start
	j=middle+1
#	Aux=[]
	Aux=A
	print ("Aux",Aux)
	for k in range(start,stop+1):
		if i>middle:
			A[k]=Aux[j]
			j=j+1
		elif j>stop:
			A[k]=Aux[i]
			i=i+1
		elif Aux[j]>Aux[i]:
			A[k]=Aux[i]
			i=i+1
		else:
			A[k]=Aux[j]
			j=j+1

#	print(A)
def mergeSort(alist):
    #print(alist)
    global comp
    #comp=0	
    if len(alist)>1:
        mid = math.ceil(len(alist)/2)
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
                comp=comp+1
            else:
                comp=comp+1
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print(alist)
    #print(comp)
    else:
        return alist
def quicksort(A):
	global comp
	comp=0
	qsort(A,0,len(A)-1)
	print("Using quick sort: ")
	print(A)
	print("Comparisons: ",comp)
	approx=math.ceil(math.log(math.factorial(len(A)),2))
	print("Approx-min: ",approx)
	
def qsort(A,start,stop):
	if start<stop:
		p=partition(A,start,stop)
		qsort(A,start,p-1)
		qsort(A,p+1,stop)
def partition(A,start,stop):
	global comp
	pivot=A[stop]
	i=start
	for j in range(start,stop):
		comp=comp+1
		if not (A[j]>pivot):
			temp=A[i]
			A[i]=A[j]
			A[j]=temp
			i=i+1
	temp2=A[i]
	A[i]=A[stop]
	A[stop]=temp2
	return i


def main():
	#command="help"
	global comp
	#A=[6,5,4,7]
	#mergeSort(A)
	#print(A)
	#print(comp)
	comp=0
	print("help-Prints this menu")
	print("exit or CTRL+D-Exits the program")
	print("sort_method int_list- Enter a sort method followed by a list of space seperated integers to sort them")
	print("Possible Sort Methods: bubblesort insertion mergesort quicksort");
#	bubblesort(A)
	command=input("Command: ");
	while command!="exit":
		if command=="help":
			print("help-Prints this menu")
			print("exit or CTRL+D-Exits the program")
			print("sort_method int_list- Enter a sort method followed by a list of space seperated integers to sort them")
			print("Possible Sort Methods: bubblesort insertion mergesort quicksort");
		#command=input();
		command_list=command.split(" ",1);
		num=[]
		if(len(command_list)>1):
			num=(command_list[1].split(' '))
			#print (num)
			method=command_list[0]
			array=[int(x) for x in num]
			#print (array)
			comp=0
			if method=='bubblesort':
				bubblesort(array)
			elif method=='insertion':
				insertion(array)
			elif method=='mergesort':
				mergesort(array)
			else:
				quicksort(array)
			#print(array)
			#print(comp)
		command=input("Command: " );

	print("Bye")
if __name__ == "__main__":
	main()
		
		
