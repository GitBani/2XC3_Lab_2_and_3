from bad_sorts import *
from good_sorts import *
from graph_funcs import length_vs_time_graph
import matplotlib.pyplot as pyplot

num_of_tests = 10_000
list_len = 50

# Insertion Sort
is_times = length_vs_time_graph(list_len, num_of_tests, insertion_sort)
pyplot.plot(is_times)

# Quick Sort:
quick_sort_times = length_vs_time_graph(list_len, num_of_tests, quicksort)
pyplot.plot(quick_sort_times)

# Merge sort:
merge_sort_times = length_vs_time_graph(list_len, num_of_tests, mergesort)
pyplot.plot(merge_sort_times)

pyplot.title('Length vs Time For Small List Lengths')
pyplot.legend(['Insertion sort', 'Quick sort', 'Merge sort'])
pyplot.ylabel('Time (seconds)')
pyplot.xlabel('Length of list')
pyplot.show()
