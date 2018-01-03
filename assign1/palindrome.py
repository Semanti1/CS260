#!/usr/bin/python3


def palindrome(chkstr):
	length=len(chkstr)
	i=0
	k=1
	while i<(length/2):
		if chkstr[i]!=chkstr[length-i-1]:
			k=0
			break;
		i=i+1
	if k==1:
		return True	
	else:
		return False

def main() :
	testwords=['undertakes', 'impassibly', 'pop', 'misericordia', 'pup', 'dinars', 'misprisions', 'tot']
	expect=[False,False,True,False,True,False,False,True]
	i=0
	success=0
	while i<8 :
		if palindrome(testwords[i])==expect[i] :
			success=success+1
		i=i+1
	if success==8:
		print("Success! Passed {0}/8 tests.".format(success))
	else:
		print("Passed {0}/8 tests".format(success))
	


if __name__ == "__main__" :
        main()

