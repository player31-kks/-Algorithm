from collections import defaultdict
string = "abadabac"
d = defaultdict(int)
for char in string:
    d[char]+=1

for key,value in d.items():
    if value == 1:
        print(key)
        break
