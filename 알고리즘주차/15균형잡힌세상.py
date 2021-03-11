memo ={
    ")":"(",
    "]":"[",
}

def is_balance(string):    
    stack =[]
    for char in string:
        if char =="(" or char =="[":
            stack.append(char)
        elif char in memo:
            if stack and stack[-1]==memo[char]:
                stack.pop()
            else:
                # 겹치는 것이 아님
                return False
    #스택이 비어있으면
    if not stack:
        return True
    else:
        return False

while True:
    string = input()
    if string ==".":
        break
    res=is_balance(string)
    if res ==True:
        print("yes")
    else:
        print("no")