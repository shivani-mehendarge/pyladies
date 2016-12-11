#!/usr/bin/env python3
def findmin(l):
	minnum = l[0]
	for nums in l:
		if nums < minnum:
			minnum = nums
	return minnum

if __name__ == '__main__':
	l1 = [ int(x) for x in input("Enter a list of integers").split()]
	print("The minimum value in the list is {0}".format(findmin(l1)))
