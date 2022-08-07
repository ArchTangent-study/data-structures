# Quickselect benchmarking.
import quickselect_1, quickselect_2, quickselect_3
import timeit
from random import randint

def bench_quickselect_1(suite):
    for numbers, k in suite:
        qs = quickselect_1.quickselect(numbers, k)

def bench_quickselect_2(suite):
    for numbers, k in suite:
        qs = quickselect_2.quickselect(numbers, k)

def bench_quickselect_3(suite):
    for numbers, k in suite:
        qs = quickselect_3.quickselect(numbers, k)

if __name__ == "__main__":
    suite_random = [
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
        ([randint(0, 10) for i in range(11)], randint(0, 10)),
    ]
    suite_sorted = [
        ([*range(11)], 1),
        ([*range(11)], 2),
        ([*range(11)], 3),
        ([*range(11)], 4),
        ([*range(11)], 5),
        ([*range(11)], 6),
        ([*range(11)], 7),
        ([*range(11)], 8),
        ([*range(11)], 9),
        ([*range(11)], 10),
    ]

    # --- Random Inputs --- #

    qs_1_random = timeit.timeit(
        'bench_quickselect_1(suite_random)',
        setup='from __main__ import bench_quickselect_1, suite_random'
    )

    qs_2_random = timeit.timeit(
        'bench_quickselect_2(suite_random)',
        setup='from __main__ import bench_quickselect_2, suite_random'
    )

    qs_3_random = timeit.timeit(
        'bench_quickselect_3(suite_random)',
        setup='from __main__ import bench_quickselect_3, suite_random'
    )

    print("QS1 (Zero Index Pivot - Recursive), Random")
    print(f"  time: {qs_1_random}")

    print("QS2 (Half Index Pivot - Recursive), Random")
    print(f"  time: {qs_2_random}")

    print("QS3 (Half Index Pivot - Iterative), Random")
    print(f"  time: {qs_3_random}")

    # --- Sorrted Inputs --- #

    qs_1_sorted = timeit.timeit(
        'bench_quickselect_1(suite_sorted)',
        setup='from __main__ import bench_quickselect_1, suite_sorted'
    )

    qs_2_sorted = timeit.timeit(
        'bench_quickselect_2(suite_sorted)',
        setup='from __main__ import bench_quickselect_2, suite_sorted'
    )

    qs_3_sorted = timeit.timeit(
        'bench_quickselect_3(suite_sorted)',
        setup='from __main__ import bench_quickselect_3, suite_sorted'
    )

    print("QS1 (Zero Index Pivot - Recursive), Sorted")
    print(f"  time: {qs_1_sorted}")

    print("QS2 (Half Index Pivot - Recursive), Sorted")
    print(f"  time: {qs_2_sorted}")

    print("QS3 (Half Index Pivot - Iterative), Sorted")
    print(f"  time: {qs_3_sorted}")
