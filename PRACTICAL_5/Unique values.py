# to count unique values inside a list
from sys import stdin

print("Enter the elements of list seperated by space: ")
l=list(map(int, stdin.readline().strip().split()))
ans=len(set(l))
print("Number of unique elements in the inputed list are ",ans) 
