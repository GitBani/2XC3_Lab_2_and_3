from good_sorts import *
from graph_funcs import *
import matplotlib.pyplot as pyplot

num_of_tests = 100
list_len = 500

# Top Down
tdms_times = length_vs_time_graph(list_len, num_of_tests, mergesort)
pyplot.plot(tdms_times)

# Bottom Up
bums_times = length_vs_time_graph(list_len, num_of_tests, bottom_up_mergesort)
pyplot.plot(bums_times)

pyplot.title('Top Down vs Bottom Up')
pyplot.legend(['Top Down Merge Sort', 'Bottom Up Merge Sort'])
pyplot.ylabel('Time (seconds)')
pyplot.xlabel('Length of list')
pyplot.show()
