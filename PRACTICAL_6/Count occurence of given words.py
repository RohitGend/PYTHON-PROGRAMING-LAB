# to count occurences of given words in a sentence
from collections import Counter
a=input("Enter a string: ")
l=list(map(str, a.split(" ")))
key=input("Enter the word to count its occurences: ")
d=Counter(l)
print("Number of occurences of",key, "in the given sentence are: ",d[key])