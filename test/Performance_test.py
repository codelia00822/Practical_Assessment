'''
Created on 2022-07-10

@author: louis
'''
import sys
import timeit
from memory_profiler import profile

import Floyd_imperative_version
import Floyd_recursive_version


NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]


# Create  memory check when execute timer
def Floyd_imperative_time():
    # Create timer for imperative version coding with arguments graph
    t = timeit.Timer("Floyd_imperative_version.floyd(graph)",
                     setup="from __main__ import Floyd_imperative_version,\
                      graph"
                     )
    # display execution time for desired numbers of runs
    print('Elapsed time for imperative code: ', t.timeit(number=100))


# Create memory check when execute timer
def Floyd_recursive_time():
    # Create timer for recursive version coding with arguments graph
    t = timeit.Timer("Floyd_recursive_version.floyd(graph)",
                     setup="from __main__ import Floyd_recursive_version,\
                      graph",
                     )
    # display execution time for desired numbers of runs
    print('Elapsed time for recursive code: ', t.timeit(number=100))


@profile(precision=6, stream=open('imperative_memory_profiler.log', 'w+'))
# memory usage check on imperative code
def Floyd_imperative_memory():
    Floyd_imperative_version.floyd(graph)

# memory usage check on recursive code


@profile(precision=6, stream=open('recursive_memory_profiler.log', 'w+'))
def Floyd_recursive_memory():
    Floyd_recursive_version.floyd(graph)


if __name__ == "__main__":
    Floyd_imperative_time()
    Floyd_recursive_time()
    Floyd_imperative_memory()
    Floyd_recursive_memory()
