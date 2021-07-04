N = int(input())
questions = list(input())

total = 0
bonus = 0
for idx,que in enumerate(questions):
    if que=="X":
        bonus = 0
    else:
        total+=(idx+1)+bonus
        bonus+=1
print(total)
        

