from collections import defaultdict
counter = defaultdict(int)
string=input()

"missing"
"m"
if len(string)==1:
    print(string.upper())
    exit(0)

"missing"
"m"
"i"
"s"
for char in string:
    counter[char.upper()]+=1
counter = {
    m : 1
    i : 2
    s : 2  
}
    
counter.items()
(m,1),(i,2),(s,2)
c=sorted(counter.items(),key=lambda x:x[1])
first,second = c[-1],c[-2]

if first[1]==second[1]:
    print("?")
else:
    print(first[0])
    
    
    