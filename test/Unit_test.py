'''
Created on 2022-07-10

@author: louis
'''

import unittest
import sys

# import function from the recursive script
from Floyd_recursive_version import shortest_path
from Floyd_recursive_version import floyd


# Functionality test on shortest_path function
class Test_Shortest_Path(unittest.TestCase):

    def test_shortest_path_function(self):
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        actual = shortest_path(1, 3, 3, graph)
        expect = 7
        # Checking the shortest path from node 1 to node 3
        # within 3 intermediates whether meets the actual of distance 7
        self.assertEqual(actual, expect, "Distance should be 7")


# Functionality test on floyd function
class Test_Floyd(unittest.TestCase):

    def test_floyd_functionality(self):
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        actual = floyd(graph)
        expect = [[0, 7, 12, 8],
                  [NO_PATH, 0, 5, 7],
                  [NO_PATH, NO_PATH, 0, 2],
                  [NO_PATH, NO_PATH, NO_PATH, 0]]
        # Checking the calculations with definition of graph
        # whether equal to the predefined result
        self.assertEqual(actual, expect)

    # Test scenario whether definition of graph contains invalid input
    def test_floyd_input_string_failure(self):
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, "string", 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        # Raise an exception if the graph definition founds unexpected "string"
        with self.assertRaises(TypeError):
            self = shortest_path(1, 2, 3, graph)

    def test_floyd_input_null_failure(self):
        NO_PATH = sys.maxsize
        graph = []
        # Checking the graph definition whether is not none
        self.assertIsNotNone(graph)

    def test_floyd_input_format_failure(self):
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        actual = graph
        expect = []
        # Checking the input format before calculation
        self.assertIs(type(actual), type(expect))

    # Test scenario if any one of the node is not exist
    def test_floya_not_exist_node_failure(self):
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        with self.assertRaises(IndexError):
            self = shortest_path(0, 5, 4, graph)

    # Test scenario whether the intermediate node exists
    def test_not_exist_intermidate_failure(self):
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        with self.assertRaises(IndexError):
            self = shortest_path(2, 0, 4, graph)

    # Checking if only one node is in the calculation
    def test_flody_only_node_failure(self):
        NO_PATH = sys.maxsize
        graph = [[0, NO_PATH, NO_PATH, NO_PATH]]
        actual = shortest_path(0, 0, 0, graph)
        expect = 0
        self.assertEqual(actual, expect, "Only one node is found")
        
    # Checking the output after calculation whether is not none
    def test_floyd_output_null_failure(self):
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        actual = floyd(graph)
        self.assertIsNotNone(actual)
        
    # Checking the output format after calculation
    def test_floyd_output_format_failure(self):
        NO_PATH = sys.maxsize
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
        actual = floyd(graph)
        expect = []
        self.assertIs(type(actual), type(expect))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
