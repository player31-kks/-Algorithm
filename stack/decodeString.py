from collections import deque

def decodeString(s:str):

    num_stack =[]
    stack =[[]]
    for idx,char in enumerate(s):
        if char.isnumeric():
            if not s[idx-1].isnumeric():
                num_stack.append([])
            num_stack[-1].append(char)
        elif char=="[":
            stack.append([])
        elif char.isalpha():
            stack[-1].append(char)
        elif char=="]":
            count = "".join(num_stack.pop())
            value = "".join(stack.pop())
            stack[-1].append(value*int(count))
    return "".join(stack[0])

if __name__ == '__main__':
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a2[c]]"))
    print(decodeString("100[leetcode]"))

