"""Implements selected algorithms and odd problems in CLRS chapter 4

This file should be imported as a module and contains the following functions:

	* max_sublist_lin - searches list for the maximum sublist in linear time

Command-line syntax: 
	$ python3 <filename>
"""

import random
import time
import math as m
import numpy as np

def max_sublist_lin(a):
	"""Searches list 'a' for its maximum sublist in linear time
	
	Args:
		a (list): list for which to find the maximum sublist 
	
	Returns:
		tuple: First element is a list of indicies of maximum sublist, 
			   second element is the maximum subsum
	"""
	
	# keep track of longest sublist inside and on the leading edge
	# reset leading edge sublist if next element is negative or 
	# a positive is preceded by a negative
	
	if (len(a) == 1):
		return ([0,1], a[0])
		
	interior_ind1 = 0
	interior_ind2 = 1
	interior_sum = a[0]
	max_sum = interior_sum
	
	lead_ind1 = 0
	lead_ind2 = 1
	lead_sum = a[0]
	
	for i in range(1, len(a)):
		if (lead_sum + a[i] > max_sum):
			max_sum = lead_sum + a[i]
			interior_ind1 = lead_ind1
			interior_ind2 = i + 1
			lead_ind2 += 1
			lead_sum += a[i]
			
		elif (a[i] < 0):
			lead_ind1 = i
			lead_ind2 = i + 1
			lead_sum = a[i]
			
		elif (a[i] > 0 and a[i-1] < 0):
			lead_ind1 = i
			lead_ind2 = i + 1
			lead_sum = a[i]
			
		else:
			lead_ind2 += 1
			lead_sum += a[i]
			
	return ([interior_ind1, interior_ind2], max_sum)

# testing functions defined in this module	
if __name__ == '__main__':
	arr = [2,-7,5,6,-1,-3,2,2,2,2,2,2,2,2,2,2,2,2,2,3,-2,5]
	result = max_sublist_lin(arr)
	print('max sublist indices: ', result[0], '\nmax sum = ', result[1])

		
