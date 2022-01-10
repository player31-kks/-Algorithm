def removeDuplicate(s:str)->str:

    stack =[]
    for char in s:
        if stack and stack[-1]==char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


if __name__ == '__main__':
    print(removeDuplicate("abbaca"))
    print(removeDuplicate("azxxzy"))