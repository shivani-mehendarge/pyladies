#!/usr/bin/env python3
def separate(list1):
	list_nums = []
	for x in list1:
		if x.isalpha() == False:
			list_nums.append(int(x))
	return list_nums

def findsum(nums_list):
	sum1 = 0
	for num in nums_list:
		sum1 += num
	return sum1

if __name__ == '__main__':
	list2 = []
	l = [x for x in input("Enter alphanumeric string ").split()]
	list2 = separate(l)
	print(findsum(list2))

