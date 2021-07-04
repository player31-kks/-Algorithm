
N =10000
selfie =[False for i in range(N+1)]

def digit_hap(num):
    s = 0
    while num>0:
        s += num%10  //2345 = (2+3+4+5 +2345) 일의자리 만들기
        num = num//10 //234 -> 23 -> 2 ->0
    return s

for i in range(1,N+1):
    if selfie[i]== False:
        //N 100
        move = i
        while True:
            if move<10:
                move = 2*move
            else:
                move = move+digit_hap(move)
            if move>N:
                break
            selfie[move] = True
            
for idx,value in enumerate(selfie):
    if value ==False and idx!=0:
        print(idx)
            