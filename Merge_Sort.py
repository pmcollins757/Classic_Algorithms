# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 00:19:28 2016

@author: DrCollins

Problem

The problem of sorting a list of numbers lends itself 
immediately to a divide-and-conquer strategy: 
split the list into two halves, recursively sort each half, 
and then merge the two sorted sublists 
(recall the problem “Merge Two Sorted Arrays”).

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

Given: A positive integer n ≤ 10**5
and an array A[1..n] of integers from −10**5 to 10**5.

Return: A sorted array A[1..n].
Sample Dataset

10
20 19 35 -18 17 -20 20 1 4 4

Sample Output

-20 -18 1 4 4 17 19 20 20 35

"""


def merge_arrays(A_arr, B_arr):

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


def merge_sort(in_list):
    half_size = round(len(in_list)/2)
    if half_size < 1:
        return in_list
    left = in_list[:half_size]
    right = in_list[half_size:]
    left = merge_sort(left)
    right = merge_sort(right)
    # if left[-1] <= right[0]:
     #    left.extend(right)
      #   return left
    result = merge_arrays(left, right)
    return result


def read_file_and_sort():
        with open("rosalind_ms.txt") as input_file:
            in_size = int(input_file.readline().strip())
            in_list = [int(x) for x in input_file.readline().split()]
        merged = merge_sort(in_list)
        with open("merge_sort_output.txt", "w") as out_file:
            out_file.write(' '.join([str(x) for x in merged]))
        return merged

print(read_file_and_sort())
