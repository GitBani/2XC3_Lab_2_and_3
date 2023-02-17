from good_sorts import *
from graph_funcs import length_vs_time_graph
import matplotlib.pyplot as pyplot


# At these current values, it might take a while to run, but it does work
num_of_tests = 10
list_len = 500

# Merge sort:
merge_sort_times = length_vs_time_graph(list_len, num_of_tests, mergesort)
pyplot.plot(merge_sort_times)

# Quick Sort:
quick_sort_times = length_vs_time_graph(list_len, num_of_tests, quicksort)
pyplot.plot(quick_sort_times)

# Heap Sort:
heap_sort_times = length_vs_time_graph(list_len, num_of_tests, heapsort)
pyplot.plot(heap_sort_times)

pyplot.title('List Length vs. Time')
pyplot.legend(['Merge sort', 'Quick sort', 'Heap sort'])
pyplot.ylabel('Time (seconds)')
pyplot.xlabel('Length of list')
pyplot.show()
