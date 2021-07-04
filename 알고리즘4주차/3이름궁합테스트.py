from collections import defaultdict
nums = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
alpha_dict =dict()

def new_name(A_cnt,B_cnt,A_name,B_name):
    limit =min(A_cnt,B_cnt)
    new_name = ""
    for idx in range(limit):
        new_name+=A_name[idx]
        new_name+=B_name[idx]
    new_name += A_name[limit:]
    new_name += B_name[limit:]
    return new_name


for idx,num in enumerate(nums):
    alpha_dict[chr(65+idx)] = num

A_cnt,B_cnt = map(int,input().split())
A_name,B_name = input().split()
name = new_name(A_cnt,B_cnt,A_name,B_name)

name_num = []
for char in name:
    name_num.append(alpha_dict[char])

while len(name_num)>2:
    for idx in range(1,len(name_num)):
        name_num[idx-1] = (name_num[idx-1]+ name_num[idx])%10
    name_num.pop()

percent = name_num[0]*10+ name_num[1]
print(f'{percent}%')