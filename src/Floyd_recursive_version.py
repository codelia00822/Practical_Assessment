'''
Created on 2022-07-10

@author: louis
'''
import sys
import itertools

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])

# Recursive function to get the shortest path


def shortest_path(start, destination, intermediate, distance):
    """
    Implementation of Floyd's algorithm using recursion
    """
    # Calculate the direct paths and exit the recursion
    # when no more intermediate nodes
    if intermediate < 0:
        return(distance[start][destination])

    # Calculate and return the shortest path from comparison
    the_shortest_path = min(shortest_path(start, destination, intermediate - 1,
                                          distance),
                            shortest_path
                            (start, intermediate, intermediate - 1, distance) +
                            shortest_path(intermediate, destination,
                                          intermediate - 1, distance))

    return the_shortest_path


def floyd(distance):

    # Calculate the path combinations for each node
    for start_node, end_node in itertools.product(range(MAX_LENGTH),
                                                  range(MAX_LENGTH)):

        # Assumes that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # Runs the shortest path to calculate the shortest path between each
        # start node and end node
        distance[start_node][end_node] = shortest_path(start_node,
                                                       end_node,
                                                       MAX_LENGTH - 1, distance
                                                       )
    # Return the distance between nodes
    return distance


if __name__ == '__main__':
    # Pass the definition of graph to floyd, then print the result.
    # Any value that have sys.maxsize has no path
    print(floyd(graph))
