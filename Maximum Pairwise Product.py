import sys

#read number of elements
n = int(input())

#take input elements and store them to list
num_list = list(map(int,input().strip().split()))[:n]

#search for fisrts and second largest integers
lar_int1 = max(num_list)
num_list.remove(lar_int1)

lar_int2 = max(num_list)

#print max pairwise product
print(lar_int1*lar_int2)
    
