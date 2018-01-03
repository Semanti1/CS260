#Mark Boady
#Drexel University 2017
#CS 260 Summer 2017

#This file tests queue.py to see if it meets the implementation guidelines.
#The goal of this file is not to prove your code in 100% correct.
#It only performs some simple tests and will not catch all possible mistakes.

#DO NOT MAKE ANY CHANGES TO THIS FILE
from node import *
from queue import *
import random

if __name__=="__main__":
    print("Step 1: Check that constructor works.")
    Q = Queue()
    if(Q==None):
        print("Variable not set.")
    else:
        print("Variable Created.")
    print("Step 2: Test Printing Empty Queue.")
    if str(Q)=="Queue Empty":
        print("Success.")
    else:
        print("Returned",str(Q),"expected","Queue Empty")
    print("Step 3: Check that the Queue is Empty.")
    if Q.empty()==True:
        print("Success")
    else:
        print("Returned",Q.empty(),"expected",True)
    print("Step 4: Add a single item to the queue.")
    Q.enqueue(1)
    if str(Q)=="[ 1 ]":
        print("Success")
    else:
        print("Returned",str(Q),"expected","[ 1 ]")
    print("Step 5: Check the Front of the queue.")
    if Q.front()==1:
        print("Success")
    else:
        print("Returned",Q.front(),"expected",1)
    print("Step 6: Check the Queue is not empty.")
    if Q.empty()==False:
        print("Success")
    else:
        print("Returned",Q.empty(),"expected",False)
    print("Step 7: Test Dequeue")
    Q.dequeue()
    if Q.empty()==True:
        print("Success")
    else:
        print("Failure: Queue is not empty! Looks like ",str(Q))
    print("Step 8: Test Added and removing 100 Random Elements")

    expected=[]
    position=0
    passed=0
    failed=0
    for x in range(0,100):
        test=random.randint(0,10000)
        expected.append(test)
        Q.enqueue(test)
    while not(Q.empty()):
        if Q.front()==expected[position]:
            passed+=1
        else:
            failed+=1
        Q.dequeue()
        position+=1
    if(failed==0):
        print("Passed",passed,"out of",(passed+failed),"tests.")
    else:
        print("Failed",failed,"out of",(passed+failed),"tests.")



