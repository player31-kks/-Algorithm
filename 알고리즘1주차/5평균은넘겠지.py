n = int(input())

for _ in range(n):
   lst= list(map(int,input().split()))
   count,score = lst[0],sorted(lst[1:])
   
   st_count = 0
   avg = sum(score)/count
   for s in score[::-1]:
      if s<=avg:
         break
      st_count+=1
   print(f'{(st_count/count)*100:.3f}%')
   print(f'{i:.3f}%')