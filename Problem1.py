'''Fredo is pretty good at dealing large numbers. So, once his friend Zeus gave him an array of N numbers , followed by Q queries which he has to answer. In each query , he defines the type of the query and the number f for which Fredo has to answer. Each query is of the following two types:
Type 0: For this query, Fredo has to answer the first number in the array (starting from index 0) such that its frequency is atleast equal to f.
Type 1: For this query, Fredo has to answer the first number in the array such that frequecy is exactly equal to f.
Now, Fredo answers all his queries but now Zeus imagines how he should verify them . So, he asks you to write a code for the same.
Note: If there is no number which is the answer to the query, output 0.
Use fast I/O.

Input :
The first line of the input contains N , the size of the array
The next line contains N space separated integers.
The next line contains Q, denoting the number of queries.
Then follow Q lines, each line having two integers type and f, denoting the type of query and the frequency for which you have to answer the query.

Output:
You have to print the answer for each query in a separate line.
SAMPLE INPUT 
6
1 2 2 1 2 3
5
0 1
0 2
1 2
1 3
0 3
SAMPLE OUTPUT 
1
1
1
2
2

'''
import os
import sys

def perform_zero(f,arr):
    
    for each in arr : 
        if arr.count(each) >= f:
            print(each)
            break

def perform_one(f,arr):
    
    for each in arr:
        if arr.count(each) == f:
            print(each)
            break
            
N = int(input())

arr = []

arr = list(map(int,input().split()))

Q = int(input())

q_mat = [[0]*2]*Q

for i in range(Q):
    q_mat[i] = list(map(int, input().split()))
    
for i in range(Q):
    
    if q_mat[i][0] == 0:
        perform_zero(q_mat[i][1],arr)
    else:
        perform_one(q_mat[i][1],arr)


        
