def minRemoveToMakeValid(s: str) -> str:
    stack = []
    answer = []

    for char in s:
        if char.isalpha():
            answer.append(char)
        elif char=="(":
            stack.append(len(answer))
            answer.append(char)
        elif char==")" and stack:
            stack.pop()
            answer.append(char)

    for value in stack:
        answer[value] =""
    return "".join(answer)



if __name__ == '__main__':
    print(minRemoveToMakeValid("lee(t(c)o)de)"))
    print(minRemoveToMakeValid("a)b(c)d"))
    print(minRemoveToMakeValid("))(("))