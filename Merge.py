# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 00:20:58 2016

@author: DrCollins

The merging procedure is an essential part of “Merge Sort” 
(which is considered in one of the next problems).

Given: A positive integer n ≤ 10**5
and a sorted array A[1..n] of integers from −10**5 to 10**5, 
a positive integer m ≤ 10**5 and a sorted array B[1..m] 
of integers from −10**5 to 10**5.

Return: A sorted array C[1..n+m]
containing all the elements of A and B.
Sample Dataset

4
2 4 10 18
3
-5 11 12

Sample Output

-5 2 4 10 11 12 18
"""

def merge_arrays():
    with open("rosalind_mer.txt") as input_file:
        A_size = int(input_file.readline().strip())
        A_arr = [int(x) for x in input_file.readline().split()]
        B_size = int(input_file.readline().strip())
        B_arr = [int(x) for x in input_file.readline().split()]
    
    merged_list = []
    while (B_arr or A_arr):
        if not A_arr:
            merged_list.extend(B_arr)
            return merged_list
        elif not B_arr:
            merged_list.extend(A_arr)
            return merged_list
        elif A_arr[0] <= B_arr[0]:
            merged_list.append(A_arr.pop(0))
        else:
            merged_list.append(B_arr.pop(0))

    return merged_list

merged = (merge_arrays())

with open("merge_arrays_output.txt", "w") as out_file:
    out_file.write(' '.join([str(x) for x in merged]))
