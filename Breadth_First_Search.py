# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 22:37:50 2016

@author: DrCollins

Problem

The task is to use breadth-first search to compute 
single-source shortest distances in an unweighted directed graph.

Given: A simple directed graph with n ≤ 10**3 vertices in the edge list format
(The first line contains two numbers, 
the number of vertices n and the number of edges m, 
each of the following m lines contains an edge given by two vertices.).

Return: An array D[1..n] where D[i] is the length 
of a shortest path from the vertex 1 to the vertex i (D[1]=0). 
If i is not reachable from 1 set D[i] to −1.

Sample Dataset

6 6
4 6
6 5
4 3
3 5
2 1
1 4

Sample Output
0 -1 2 1 3 2

"""

def breadth_search():
    from collections import defaultdict
    adjacent = defaultdict(list)
    result  = []

    with open("BFS_sample.txt", "r") as edge_file:
        vertex_count, edge_count = edge_file.readline().split()
        #print vertex_count, edge_count
        for line in edge_file:
            key, value = line.split()
            adjacent[int(key)].append(int(value))
            
    print("adjacent:", adjacent)
    
    length = 1
    level = {1:0}
    parent = {1:None}
    next_lvl = [1]    
    while next_lvl:
        new_lvl = []
        for u in next_lvl:
            for v in adjacent[u]:
                if v not in level:
                    level[v] = length
                    parent[v] = u
                    new_lvl.append(v)
        next_lvl = new_lvl
        length += 1
    
    for x in range(1, int(vertex_count) + 1):
        if x not in level:
            result.append(-1)
        else:
            result.append(level[x])
    print("parent:", parent)
    return result
    
breadth_output = breadth_search()

with open("BFS_output.txt", "w") as out_file:
    out_file.write(' '.join([str(x) for x in breadth_output]))


    