from good_sorts import *
from graph_funcs import *
import matplotlib.pyplot as plot
from math import log10

runs = 10
list_len = 500
swaps = int(list_len * log10(list_len) / 2)

# Quick Sort:
quick_sort_times = disorderedness_vs_time(list_len, swaps, runs, quicksort)
plot.plot(quick_sort_times)

# Merge Sort:
merge_sort_times = disorderedness_vs_time(list_len, swaps, runs, mergesort)
plot.plot(merge_sort_times)

# Heap Sort:
heap_sort_times = disorderedness_vs_time(list_len, swaps, runs, heapsort)
plot.plot(heap_sort_times)

plot.title('Disorderness vs Time')
plot.ylabel('Time(seconds)')
plot.xlabel('No. of swaps')
plot.legend(['Quick sort', 'Merge Sort', 'Heap Sort'])
plot.show()
