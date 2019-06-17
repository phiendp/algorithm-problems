# Re-arrange Array Elements

## Introduction
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1.

## Approach
To re-arrange the list of digits, we will use merge sort to sort the list in reversed order. Then, we will iterate the sorted list and take turn to add each digit to the first or second list. Finally, we convert the two created lists to number and that is our final results.

## Analysis
Let N be the number of digits in the input array.
- For time complexity, since we are using merge sort algorithm, the time complexity will be O(NlogN).
- For the space complexity, the overall complexity is O(N), but note that we need additional space for the two created lists after performing merge sort.
