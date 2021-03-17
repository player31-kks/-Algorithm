def func(string):
    if string == ')':
        return '('
    if string == ']':
        return '['
    
data = input().split('.')
data.pop()
for string in data:
    global stack
    stack = []
    flag = True
    for x in string:
        if x == '[' or x == '(':
            stack.append(x)
        if x == ')' or x == ']':
            if stack != []:
                if stack.pop() == func(x):
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    if flag == True:
        print('yes')
    else:
        print('no')