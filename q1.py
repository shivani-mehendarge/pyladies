#!/usr/bin/env python3
def listsum(l1):
	sum1 = 0
	for num in l1:
		sum1 += num
	return sum1

if __name__ == '__main__':
	
	list1 = [int(x) for x in input("Enter a list of numbers ").split()]
	print(listsum(list1))	
