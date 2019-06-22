# Dutch National Flag Problem

## Introduction
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.


## Approach
One way to solve this problem in a single traversal is by keeping two pointers for index of found 0 and found 2 (1 integers will be kept in place), then we increase the index for 0 integers or decrease the index for 2 integers while traversing the array, and swap the numbers.

## Analysis
Let N be the number of elements in the array.
Then, the time complexity will be O(N), since we will iterate through the whole array. And the space complexity will be O(N).
