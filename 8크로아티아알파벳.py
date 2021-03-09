check=["c=","c-","dz=","d-","lj","nj","s=","z="]
string = input()

for ch in check:
    string=string.replace(ch,"*")
print(len(string))


