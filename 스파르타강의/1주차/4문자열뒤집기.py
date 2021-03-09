string = input()

zero_part =0
one_part = 0

temp ="x"
for char in string:
    if temp!=char:
        temp = char
        if temp=='0':
            zero_part+=1
        else:
            one_part+=1
print(min(zero_part,one_part))