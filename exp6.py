from good_sorts import *
from graph_funcs import *
import matplotlib.pyplot as pyplot

num_of_tests = 100
list_len = 500

# Traditional
regular_qs_times = length_vs_time_graph(list_len, num_of_tests, quicksort)
pyplot.plot(regular_qs_times)

# Dual Pivot
dual_qs_times = length_vs_time_graph(list_len, num_of_tests, dual_quicksort)
pyplot.plot(dual_qs_times)

pyplot.title('One vs Two Pivots')
pyplot.legend(['One pivot quick sort', 'Two pivot quick sort'])
pyplot.ylabel('Time (seconds)')
pyplot.xlabel('Length of list')
pyplot.show()
