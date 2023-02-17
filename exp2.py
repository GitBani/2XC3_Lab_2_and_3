from bad_sorts import *
from graph_funcs import length_vs_time_graph
import matplotlib.pyplot as pyplot

num_of_tests = 10
list_len = 500

# Bubble Sort:
bubble_sort_times = length_vs_time_graph(list_len, num_of_tests, bubble_sort)
pyplot.plot(bubble_sort_times)
bubble_sort2_times = length_vs_time_graph(list_len, num_of_tests, bubble_sort2)
pyplot.plot(bubble_sort2_times)
pyplot.title('List Length vs. Time')
pyplot.legend(['Traditional bubble sort', 'Optimized bubble sort'])
pyplot.ylabel('Time (seconds)')
pyplot.xlabel('Length of list')
pyplot.show()

# Selection Sort:
selection_sort_times = length_vs_time_graph(list_len, num_of_tests, selection_sort)
pyplot.plot(selection_sort_times)
selection_sort2_times = length_vs_time_graph(list_len, num_of_tests, selection_sort2)
pyplot.plot(selection_sort2_times)
pyplot.title('List Length vs. Time')
pyplot.legend(['Traditional selection sort', 'Optimized selection sort'])
pyplot.ylabel('Time (seconds)')
pyplot.xlabel('Length of list')
pyplot.show()
