import timeit
from bad_sorts import create_random_list, create_near_sorted_list


def length_vs_time_graph(n, trials, algo):
    t = []
    for i in range(1, n + 1):
        time = 0
        for j in range(trials):
            L = create_random_list(i, 10_000)
            start = timeit.default_timer()
            algo(L)
            end = timeit.default_timer()
            time += end - start
        t.append(time / trials)
    return t


def disorderedness_vs_time(n, swaps, trials, sorting_algo):
    t = []
    for i in range(swaps + 1):
        time = 0
        for j in range(trials):
            L = create_near_sorted_list(n, 10000, i)
            start = timeit.default_timer()
            sorting_algo(L)
            end = timeit.default_timer()
            time += end - start
        t.append(time / trials)
    return t
