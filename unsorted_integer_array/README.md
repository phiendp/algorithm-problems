# Max and Min in a Unsorted Array

## Introduction
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

## Approach
We will iterate the input list and keep track of two variables, min and max. If the current number is larger than the max value, then the max value will be updated to that number. If the current number is less than the min value, then the min value will be updated to that number.

## Analysis
Let N be the number of element in the input array. Since we need to iterate through the input array, the time complexity will be O(N). The space complexity is O(1), since we don't need any additional data structure for solving this problem.
