# Search in a rotated array

## Introduction
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.


## Approach
- For this problem, we will apply binary search on the left and right half of the rotated array.
- First, we will find the pivot number in the array by checking the middle element of the array.
- After locating the pivot number, we then perform binary search on the left and right subarrays, based on that pivot number.

## Analysis
Let N be the number of elements in the array. In this approach, finding the pivot number will take O(logN)complexity, and binary searches take time complexity of O(logN) as well. Therefore, the overall time complexity is O(logN). The space complexity will be O(N).
