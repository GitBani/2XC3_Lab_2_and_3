from bad_sorts import *
from graph_funcs import length_vs_time_graph
import matplotlib.pyplot as pyplot

# At these current values, it might take a while to run, but it does work
num_of_tests = 10
list_len = 500

# Bubble Sort:
bubble_sort_times = length_vs_time_graph(list_len, num_of_tests, bubble_sort)
pyplot.plot(bubble_sort_times)

# Selection Sort:
selection_sort_times = length_vs_time_graph(list_len, num_of_tests, selection_sort)
pyplot.plot(selection_sort_times)

# Insertion Sort:
insertion_sort_times = length_vs_time_graph(list_len, num_of_tests, insertion_sort)
pyplot.plot(insertion_sort_times)

pyplot.title('List Length vs. Time')
pyplot.legend(['Bubble sort', 'Selection sort', 'Insertion sort'])
pyplot.ylabel('Time (seconds)')
pyplot.xlabel('Length of list')
pyplot.show()
