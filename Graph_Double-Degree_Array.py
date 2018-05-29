# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 01:59:15 2015

@author: Dr Patrick Collins
Graph Double-Degree Array 
Topics: Graphs

Problem
Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

Given: A simple graph with n ≤ 10**3 vertices in the edge list format
(The first line contains two numbers, 
the number of vertices n and the number of edges m, 
each of the following m lines contains an edge given by two vertices.).

Return: An array D[1..n] where D[i] is the sum of 
the degrees of i's neighbors.

Sample Dataset:

5 4
1 2
2 3
4 3
2 4

Sample Output:

3 5 5 5 0

"""



def deg_array():
    from collections import defaultdict
    adjacent = defaultdict(list)
    result = {}

    with open("rosalind_ddeg.txt", "r") as edge_file:
        vertex_count, edge_count = edge_file.readline().split()
        #print vertex_count, edge_count
        for line in edge_file:
            key, value = line.split()
            adjacent[key].append(value)
            adjacent[value].append(key)
    
    for vertex, neighbors_list in adjacent.iteritems():
        neighbor_len_total = sum([len(adjacent[neighbor]) 
                                    for neighbor in neighbors_list])
        result[vertex] = neighbor_len_total

    val_list = []    
    for x in range(1, int(vertex_count) + 1):
        str_x = str(x)
        if str_x in result:
            val_list.append(str(result[str_x]))
        else:
            val_list.append('0')
    
    with open("graph_double_deg_out.txt", "w") as deg_out_file:
        deg_out_file.write(' '.join(val_list))
    
    return len(val_list)


print(deg_array())


