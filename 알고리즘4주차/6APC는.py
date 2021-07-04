N,L,K = map(int,input().split())

question =[]
for _ in range(N):
    easy,hard = map(int,input().split())
    question.append((easy,hard))
question.sort(key=lambda x:x[1])

total =0
for easy,hard in question:
    if L>=hard:
        total+=140
        K-=1
    elif easy<=L<hard:
        total+=100
        K-=1
    if K==0:
        break
print(total)
        