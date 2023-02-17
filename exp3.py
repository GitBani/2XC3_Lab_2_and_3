from bad_sorts import *
from graph_funcs import *
import matplotlib.pyplot as plot
from math import log10

runs = 10
list_len = 1000
swaps = int(list_len * log10(list_len) / 2)

# Bubble Sort:
bubble_sort_times = disorderedness_vs_time(list_len, swaps, runs, bubble_sort)
plot.plot(bubble_sort_times)

# Selection Sort:
selection_sort_times = disorderedness_vs_time(list_len, swaps, runs, selection_sort)
plot.plot(selection_sort_times)

# Insertion Sort:
insertion_sort_times = disorderedness_vs_time(list_len, swaps, runs, insertion_sort)
plot.plot(insertion_sort_times)

plot.title('Disorderness vs Time')
plot.ylabel('Time(seconds)')
plot.xlabel('No. of swaps')
plot.legend(['Bubble sort', 'Selection Sort', 'Insertion Sort'])
plot.show()
