"""Implements key algorithms and odd problems in CLRS chapter 2

This file should be imported as a module and contains the following functions:

	* bin_ser - searches sorted list for specified element
	* gen_rand_list - generates a list of random entries
	* insertion_sort - sorts a list using the insertion sort algorithm
	* select_sort - sorts a list using the selection sort algorithm
	* merge_sort - sorts a list using the merge sort algorithm
	* merge_sort_ins - sorts a list using merge sort with insertion sort for 
					   small sublists
	* merge - auxillary function used by merge_sort: merges two sorted lists 
	          into a sorted list
	* search_sum - implements the algorithm described in exercise 2.3-7 in 
	               O(n*log(n)) time

Command-line syntax: 
	$ python3 <filename>
"""

import random
import time
import math as m
import numpy as np
import matplotlib.pyplot as plt

def bin_ser(a, e, f, l):
	"""Searches sorted sublist of ints for element e

	Args:
		a (list): Sorted sublist of ints to be searched
		e (int): Element of a to be searched for
		f (int): First index of the sublist of a to be searched
		l (int): Final index of the sublist of a to be searched
		
	Returns:
		int: The index of e if e is in a; -1 if e is not in a
	"""
	
	if (len(a) == 1):
		if (a[0] == e):
			return f
		else:
			return -1
	else:
		if (e > a[len(a)//2]):
			return bin_ser(a[len(a)//2:], e, f + len(a)//2, l)
		elif (e == a[len(a)//2]):
			return (f + len(a)//2)
		else:
			return bin_ser(a[:len(a)//2], e, f, f + len(a)//2)
			


def gen_rand_list(seed = 11, size = 1000):
	"""Generates a list of random integers
	
	Args:
		seed (int): The seed to be used by the random class
		size (int): The size of the generated list	
		
	Returns:
		list: A list of random integers
	"""
	
	#random.seed(seed)
	rand_list = [None] * size
	
	for i in range(0, size):
		rand_list[i] = random.randint(-100, 100)
		
	return rand_list

def insertion_sort(lis):
	"""Sorts a list using the insertion sort algorithm
	
	Args:
		lis (list): The list to be sorted
	"""
	
	for i in range(1, len(lis)):
		elem = lis[i]
		j = i
		while (j > 0 and elem < lis[j - 1]):
			lis[j] = lis[j - 1]
			j -= 1

		lis[j] = elem
		
def select_sort(lis):
	"""Sorts a list using the selection sort algorithm
	
	Args:
		lis (list): The list to be sorted
	"""
	
	for j in range(0, len(lis)):
		min = lis[j]; idx = j
		for k in range(j+1, len(lis)):
			if lis[k] < min:
				min = lis[k]; idx = k
				
		temp = lis[j]; lis[j] = min; lis[idx] = temp
		
def merge_sort(A, p, r):
	"""Sorts a sublist using the merge sort algorithm
	
	Args:
		A (list): The list to be sorted
		p (int): the first index of the sublist of A to be sorted (inclusive)
		r (int): the last index of the sublist of a to be sorted (inclusive)
	"""
	
	if p < r:
		q = math.floor((p+r)/2)
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		merge(A, p, q, r)
		
def merge_sort_ins(A, p, r):
	"""Sorts a sublist using the merge sort algorithm with insertion sort for small sublists
	
	Args:
		A (list): The list to be sorted
		p (int): the first index of the sublist of A to be sorted (inclusive)
		r (int): the last index of the sublist of a to be sorted (inclusive)
	"""
	
	# For sublists of size less than or equal to log_2(len(A)), use insertion
	# sort; for larger sublists use merge sort
	
	cutoff = m.floor(m.log(len(A),2))
	
	if (len(A) <= cutoff):
		insertion_sort(A[p:(r+1)])
	else:	
		if p < r:
			q = math.floor((p+r)/2)
			merge_sort(A, p, q)
			merge_sort(A, q+1, r)
			merge(A, p, q, r)
		
def merge(A, p, q, r):
	"""Merges two sorted sublists of A 
	
	Args:
		A (list): The list containing the two sorted sublists
		p (int): The first index of the first sorted sublist (inclusive)
		q (int): The last index of the first sorted sublist (inclusive)
		r (int): The final index of the second sorted sublist (inclusive)
	"""
	
	n1 = q - p + 1
	n2 = r - q
	L = n1*[0]
	R = n2*[0]

	for i in range(1, n1+1):
		L[i - 1] = A[p + i - 1]
	for j in range(1, n2+1):
		R[j - 1] = A[q + j]
	L.append('s')
	R.append('s')
	i = 0
	j = 0
	for k in range(p, r + 1):
		if (L[i] == 's'):
			A[k] = R[j]
			j += 1
		elif (R[j] == 's'):
			A[k] = L[i]
		elif (L[i] < R[j]):
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
			
def search_sum(a, x):
	"""Search list a of ints for two elements that sum to x
	
	Args:
		a (list): The list of ints to be searched 
	    x (int): The desired sum to be searched for
	        
	Returns: 
		tuple: Contains the two elements of a that sum to x
		None: If there are no two elements of a that sum to x
	"""
	
	found = False
	merge_sort(a, 0, len(a) - 1)
	first_elem_tup = 0
	second_elem_tup = 0
	for i in range(0, len(a) - 1):
		#print(a)
		candidate = a[i]
		#print(candidate)
		goal = x - candidate
		match_idx = bin_ser(a[i:], goal, i, len(a)-1)
		#print(match_idx)
		if (match_idx != -1):
			first_elem_tup = candidate
			second_elem_tup = a[match_idx]
			found = True
			break
			
	if (found):
		return (first_elem_tup, second_elem_tup)
	else:
		return None
		
			
