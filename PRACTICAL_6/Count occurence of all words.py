# to count occurences of all words in a sentence

from collections import Counter
a=input("Enter a string: ")
l=list(map(str, a.split(" ")))
d=Counter(l)
print(d)
print("Number of occurences of each word in the given sentence are: ")
for i in d:
    print(i,d[i],sep=': ')