n = int(input())
result = n
new_n =-1
count =0


while True:
    m = (n//10+n%10) #75  m=12  n//10 -십의자리 n%10 - 일의자리
    new_n = (n%10)*10+m%10 #new_n = 5*10 + 2 =52
    count+=1
    if result == new_n:
        print(count)
        break
    n = new_n