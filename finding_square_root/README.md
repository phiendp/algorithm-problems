# Finding the Square Root of an Integer

## Introduction
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.


## Approach
By apply binary search, we will search for the floored squared number, in order to calculate the square root of the given number.

## Analysis
Let N be the input number. Then, the time complexity will be O(logN), since we are applying binary search algorithm. The space complexity will be constant O(1).
