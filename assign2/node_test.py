#Mark Boady
#Drexel University 2017
#CS 260 Summer 2017

#This file tests node.py to see if it meets the implementation guidelines.
#The goal of this file is not to prove your code in 100% correct.
#It only performs some simple tests and will not catch all possible mistakes.

#DO NOT MAKE ANY CHANGES TO THIS FILE
from node import *

if __name__=="__main__":
    value=10
    ptr=None
    expected_str="[ 10 ]"

    print("Step 1: Creating a new code using Constructor.")
    test_node = Node(value,None)
    if(test_node!=None):
        print("Object Created.")
    else:
        print("Variable is None.")
    print("Step 2: Check the value of the node is correct.")
    if test_node.getValue()==value:
        print("Correct Value")
    else:
        print("Incorrect Value. Your Code Returned",test_node.getValue(),"but should have returned",value)
    print("Step 3: Check the next pointer is correct.")
    if test_node.getNext()==ptr:
        print("Correct Next Pointer")
    else:
        print("Incorrect Next Pointer. Your Code Returned",test_node.getNext(),"but should have returned",ptr)
    print("Step 4: Check that the str command is correct.")
    if str(test_node)==expected_str:
        print("Correct str function.")
    else:
        print("Incorrect str function. Your Code Returned",str(test_node),"but should have returned",expected_str)
    print("Step 5: Check that value can be changed.")
    test_node.setValue(2*value)
    if(test_node.getValue()==2*value):
        print("Value Updated Correctly.")
    else:
        print("Value failed to update. You code has value",test_node.getValue(),"but should have",2*value)

    print("Step 6: Check if Next can be changed.")
    second_node=Node(12,None)
    test_node.setNext(second_node)
    if(test_node.getNext()==second_node):
        print("Next Changed Correctly.")
    else:
        print("Next failed to update. Your code has next",test_node.getNext(),"but should have",second_node)

    print("Step 7: Make a Linked List.")
    front = Node(1,None)
    pos = front
    expected="[ 1 ]"
    for x in range(2,11):
        next = Node(x,None)
        pos.setNext(next)
        pos=next
        expected+="[ "+str(x)+" ]"
    #Print List
    start = front
    result=""
    while(start != None):
        result+=str(start)
        start=start.getNext()
    print("Your list looks like:",result)
    if result==expected:
        print("This is correct.")
    else:
        print("This is incorrect. Should look like:",expected)
