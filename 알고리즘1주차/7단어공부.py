from collections import defaultdict
counter = defaultdict(int)
string=input()

if len(string)==1:
    print(string.upper())
    exit(0)


for char in string:
    counter[char.upper()]+=1


c=sorted(counter.items(),key=lambda x:x[1])
first,second = c[-1],c[-2]

if first[1]==second[1]:
    print("?")
else:
    print(first[0])
    
    
    