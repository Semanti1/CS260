#!/usr/bin/env python3

from palindrome import palindrome
def main():
	print("Welcome to Palindrome Checker!")
	print("Enter a word. The program will tell you if it is a palindrome.")
	print("To quit enter a blank line.")
	line = input("Enter word to check: ")
	while  line:
		print ('The word is a palindrome: {0}'.format((palindrome(line))))
		line = input("Enter word to check: ")
if __name__ == "__main__":
    main()
	

