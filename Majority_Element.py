# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 22:33:56 2016

@author: DrCollins

An array A[1..n] is said to have a majority element if 
more than half of its entries are the same.

Given: A positive integer k ≤ 20, a positive integer n ≤ 10**4, 
and k arrays of size n containing positive integers not exceeding 10**5.

Return: For each array, output an element of this 
array occurring strictly more than n/2
times if such element exists, and "-1" otherwise.

Sample Dataset
4 8
5 5 5 5 5 5 5 5
8 7 7 7 1 7 3 7
7 1 6 5 10 100 1000 1
5 1 6 7 1 1 10 1

Sample Output
5 7 -1 -1
"""

import collections
def majority_elem():
    maj_elem_list = []
    with open("rosalind_maj.txt") as input_file:
        k, n = [int(x) for x in input_file.readline().split()]
        for x in range(k):
            arr = [int(x) for x in input_file.readline().split()]
            majelem, elemcnt = collections.Counter(arr).most_common(1)[0]
            if elemcnt > n/2:
                maj_elem_list.append(majelem)
            else:
                maj_elem_list.append(-1)
    with open("maj_elem_output.txt", "w") as out_file:
        out_file.write(' '.join([str(x) for x in maj_elem_list]))
    return maj_elem_list

print(majority_elem())