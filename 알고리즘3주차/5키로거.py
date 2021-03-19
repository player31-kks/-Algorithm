T = int(input())

for _ in range(T):
    keyLogger = input()
    stack =[]
    tempt_stack =[]
    for char in keyLogger:
        if char=="<":
            if stack:
                key = stack.pop()
                tempt_stack.append(key)
        elif char==">":
            if tempt_stack:
                key = tempt_stack.pop()
                stack.append(key)
            pass
        elif char=="-":
            if stack:
                stack.pop()
        else:
            stack.append(char)
    while tempt_stack:
        key = tempt_stack.pop()
        stack.append(key)
        
    print("".join(stack))