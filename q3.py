#!/usr/bin/env python3
def findlength(mystring):
	count = 0
	for c in mystring:
		count += 1
	return count

if __name__ == '__main__':
	s = input("Enter a String: ")
	print("The length of the string is {0}".format(findlength(s)))
