# -*- coding: utf-8 -*-
"""
Created on Tue May 30 00:13:13 2017

@author: DrCollins

Problem:
An inversion of an array A[1..n]
is a pair of indices (i,j) such that 1 ≤ i < j ≤ n and A[i] > A[j]. 
The number of inversions shows how far the array is from being sorted: 
if it is already sorted then there are no inversions, 
whereas if it is sorted in reverse order then the number of inversions 
is maximal.

Given: A positive integer n ≤ 10^5
and an array A[1..n] of integers from −10^5 to 10^5.

Return: The number of inversions in A.
Sample Dataset
5
-6 1 15 8 10

Sample Output
2

Use Merge Sort. Count every time left is greater than right?

"""


def count_inv():

    with open("rosalind_inv.txt", "r") as file_id:
        Array_size = file_id.readline()
        A = [int(x) for x in file_id.readline().split()]
    
    print(Array_size)
    invs = 0
    


out_invs = count_inv()
print(out_invs)
with open("rosalind_inv_output.txt", "w") as out_file:
    out_file.write(' '.join([str(x) for x in out_invs]))
