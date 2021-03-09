# a = int(input())
# b = input()

# for i in b[::-1]:
#   print(a*int(i))
# print(a*int(b))


# 정석
b = int(input())
a = int(input())
digit = a
while digit>0: 
    print(b*(digit%10)) # 일의자리 추출 
    digit = digit//10   # 736 -> 73 -> 7 ->0
print(a*b)
