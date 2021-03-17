string=input()

result = 0
for char in string:
    num = int(char)
    if num<2:
        result+=num
    else:
        result*=num
