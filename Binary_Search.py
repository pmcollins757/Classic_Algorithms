# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 01:51:44 2015

@author: Dr Patrick Collins
The problem is to find a given set of keys in a given array.

Given: Two positive integers n ≤ 10**5 and m ≤ 10**5, 
a sorted array A[1..n] of integers from −10**5 to 10**5 
and a list of m integers −10**5 ≤ k1,k2,...,km ≤ 10**5.

Return: For each ki, output an index 1 ≤ j ≤ n such that 
A[j] = ki or "-1" if there is no such index.

Sample Dataset:

5
6
10 20 30 40 50
40 10 35 15 40 20

Sample Output:

4 1 -1 -1 4 2

"""
def binsearch():
    with open("rosalind_bins.txt", "r") as bins_file:
        lenA = int(bins_file.readline())
        lenk = int(bins_file.readline())
        A = [int(x) for x in bins_file.readline().split()]
        k = [int(x) for x in bins_file.readline().split()]
    output = []
    #print(lenA, lenk)
    for ki in k:
        i = round(lenA / 2)
        mini = 0
        maxi = lenA
        while (mini < i < maxi) and ki != A[i]:
            if (ki < A[i]):
                maxi = i
                i = round((mini + maxi) / 2)
            elif (ki > A[i]):
                mini = i 
                i = round((mini + maxi) / 2)
        else:
            if ki == A[i]:
                output.append(i + 1)
            else:
                output.append(-1)
    with open("bins_output.txt", "w") as out_file:
        out_file.write(' '.join([str(x) for x in output]))

    return

binsearch()
