# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:09:53 2015

@author: Dr Patrick Collins
Graph Degree Array

Problem
In an undirected graph, 
the degree d(u) of a vertex u is the number of neighbors u has, 
or equivalently, the number of edges incident upon it.

Given: A simple graph with n ≤ 10**3 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the degree of vertex i.

Sample Dataset:
(The first line contains two numbers, 
the number of vertices n and the number of edges m, 
each of the following m lines contains an edge given by two vertices.)

6 7
1 2
2 3
6 3
5 6
2 5
2 4
4 1

Sample Output:

[2 4 2 2 2 2]

"""

def deg_array():
    from collections import Counter
    total = Counter()
    with open("rosalind_deg.txt", "r") as edge_file:
        vertex_count, edge_count = edge_file.readline().split()
        print vertex_count, edge_count
        for line in edge_file:
            total.update([int(i) for i in line.split()])
    val_list = [str(val) for key, val in sorted(total.items())]
    with open("graph_deg_out.txt", "w") as deg_out_file:
        deg_out_file.write(' '.join(val_list))
    return 


deg_array()

