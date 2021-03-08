import numpy as np
import matplotlib.pyplot as plt
import time
import sorting_ch2 as sc2

#randlist = sc2.gen_rand_list(size = 50)
#print(randlist)
#sc2.merge_sort_ins(randlist, 0, len(randlist) - 1)
#print(randlist)

#mylist = [1,4,5,7,8,9,44]
#print("index of 444 in the list: ", bin_ser(mylist, 444, 0, len(mylist) - 1))

#mylist2 = [-4,3,5,-3, 7,9]
#mylist3 = gen_rand_list(size = 10)
#print("which elements of ", mylist3, " sum to 4? Answer: ", 
	   #search_sum(mylist3, 4))

#randomlist = gen_rand_list(size = 8000)
#start = time.perf_counter()
#select_sort(randomlist)
#end = time.perf_counter()
#print ('\nTime taken by select sort: ',"%.20f" % (end - start))

#randomlist = gen_rand_list(size = 8000)
#start = time.perf_counter()
#merge_sort(randomlist, 0 , len(randomlist) - 1)
#end = time.perf_counter()
#print ('\nTime taken by merge sort: ',"%.20f" % (end - start))

sizes = [10,20, 30,40, 50, 60, 70, 80, 90, 100, 200, 300, 400,
		500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 10000, 50000]
times_ins = np.zeros(len(sizes))
times_merge = np.zeros(len(sizes))
times_merge_ins = np.zeros(len(sizes))

for i in range(0, len(sizes)):
	random_list = sc2.gen_rand_list(size = sizes[i])
	start = time.perf_counter()
	sc2.insertion_sort(random_list)
	end = time.perf_counter()
	times_ins[i] = end - start
	
	random_list = sc2.gen_rand_list(size = sizes[i])
	start = time.perf_counter()
	sc2.merge_sort(random_list, 0, len(random_list) - 1)
	end = time.perf_counter()
	times_merge[i] = end - start
	
	random_list = sc2.gen_rand_list(size = sizes[i])
	start = time.perf_counter()
	sc2.merge_sort_ins(random_list, 0 , len(random_list) - 1)
	end = time.perf_counter()
	times_merge_ins[i] = end - start
	
	
plt.plot(sizes, times_ins, 'ro', label = 'ins') 
plt.plot(sizes, times_merge, 'bo', label = 'merge')
plt.plot(sizes, times_merge_ins, 'go', label = 'merge_ins')
plt.title('Merge sort vs insertion sort')
plt.xlabel('Problem size (elements in random array)')
plt.ylabel('time (s)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()



