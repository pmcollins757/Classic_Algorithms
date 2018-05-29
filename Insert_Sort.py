# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:50:26 2016

@author: DrCollins

Use Insertion Sort to sort list a list of integers, 
tracking the number of swaps used.

for i = 2:n,
    for (k = i; k > 1 and a[k] < a[k-1]; k--)
        swap a[k,k-1]
    → invariant: a[1..i] is sorted
end

Given: A positive integer n ≤ 10**3 and an array A[1..n] of integers.

Return: The number of swaps performed by insertion sort algorithm on A[1..n].

Sample Dataset

6
6 10 4 5 1 2

Sample Output

12

"""

def ins_sort():
    with open("rosalind_ins.txt") as input_file:
        arr_size = int(input_file.readline())
        arr = [int(x) for x in input_file.readline().split()]
    
    swap_cnt = 0
    for i in range(1, arr_size):
        k = i
        while (k >= 1) and (arr[k] < arr[k - 1]):
            arr[k - 1], arr[k] = arr[k], arr[k - 1]
            swap_cnt += 1
            k -= 1
    return swap_cnt

print(ins_sort())
