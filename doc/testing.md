### Running tests

This project there are two main tests:

- Unit tests
- Performance test

Both the unit and performance tests can be execute individually in Eclipse console


## Unit tests

The unit test is run under Eclipse console. 


The console expected outcome is:

```bash

..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK

```


## Performance tests

The performance test is using the `timeit` module that measures the execution
of time of small code snippets. In this case, the script compares the runtime
of the initial `floyd_imperative.py` file and `floyd_recursive.py`.

If you are running a Unix system, ensure you have run the `chmod` command to
change the access permissions. Then, in the `tests` directory run:


The performance test is run under Eclipse console. It will generate two <name>_memory_profile.log for memory usage comparsion.

The console result is expected as:

```bash

[[0, 7, 12, 8], [9223372036854775807, 0, 5, 7], [9223372036854775807, 9223372036854775807, 0, 2], [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]
[[0, 7, 12, 8], [9223372036854775807, 0, 5, 7], [9223372036854775807, 9223372036854775807, 0, 2], [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]
                                                                .
                                                                .	
                                                                .
[[0, 7, 12, 8], [9223372036854775807, 0, 5, 7], [9223372036854775807, 9223372036854775807, 0, 2], [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]															
[[0, 7, 12, 8], [9223372036854775807, 0, 5, 7], [9223372036854775807, 9223372036854775807, 0, 2], [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]
Elapsed time for imperative code:  0.023119600024074316
Elapsed time for recursive code:  0.5403205999173224

```

imperative_memory_profiler.log and recursive_memory_profiler1.log will record the memory usage when execute the function in desried numbers of runs.

Sample as below:

Filename: 

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    21  19.5039 MiB  19.5039 MiB           1   @profile(precision=4, stream=open('imperative_memory_profiler.log', 'w+'))
    22                                         # Create  memory check when execute timer
    23                                         def Floyd_imperative_time():
    24                                             # Create timer for imperative version coding with arguments graph
    25  19.5195 MiB   0.0156 MiB           2       t = timeit.Timer("Floyd_imperative_version.floyd(graph)",
    26  19.5078 MiB   0.0000 MiB           1                        setup="from __main__ import Floyd_imperative_version,\
    27                                                               graph"
    28                                                              )
    29                                             # display execution time for desired numbers of runs
    30  19.5312 MiB   0.0117 MiB           1       print('Elapsed time for imperative code: ', t.timeit(number=100))


Filename: 

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    33  19.5430 MiB  19.5430 MiB           1   @profile(precision=4, stream=open('recursive_memory_profiler1.log', 'w+'))
    34                                         # Create memory check when execute timer
    35                                         def Floyd_recursive_time():
    36                                             # Create timer for recursive version coding with arguments graph
    37  19.5469 MiB   0.0039 MiB           2       t = timeit.Timer("Floyd_recursive_version.floyd(graph)",
    38  19.5430 MiB   0.0000 MiB           1                        setup="from __main__ import Floyd_recursive_version,\
    39                                                               graph",
    40                                                              )
    41                                             # display execution time for desired numbers of runs
    42  19.5469 MiB   0.0000 MiB           1       print('Elapsed time for recursive code: ', t.timeit(number=100))


