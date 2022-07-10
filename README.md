# Conversion to recursive of Floyd Warshall's Algorithm

This assessment rewrites Floyd Warshall’s Algorithm from imperative version to recursive version within Python.

For more information of this assessment, see 'doc/practical_assessment.md'

## Quick start
Please refer to the requirments.txt which has listed the required files to install. It is recommended to run under Eclipse console as the scripting in developed under Eclipse IDE with PyDev module.

However, there is still a way to run the main codes in Windows, open the CMD and navigate to the directory 'src’ and execute the following command:

floyd_recursive_version.py

The output will print in your terminal and it is expected the result like below:

[[0, 7, 12, 8], [9223372036854775807, 0, 5, 7], [9223372036854775807, 9223372036854775807, 0, 2], [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]

## Code testing

This code runs a simple set of unit and performance tests. Please refer to the directory 'test' for more information. Documentation regards the tests are stated in directory 'doc'.

The testing code can be run individually.


## License

Copyright 2022 Chun WONG

Licensed under the Apache License, Version 2.0

For full license documentation, you may refer to 'license' or obtain a copy at

    http://www.apache.org/licenses/LICENSE-2.0
    

Last modify by Chun WONG 2022-07-10
