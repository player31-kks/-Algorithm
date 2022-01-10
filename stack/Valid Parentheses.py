from collections import defaultdict

def isValid(s: str) -> bool:
    bracket = {
        '(': ')',
        '{': '}',
        '[': ']'
    }


    stack = []
    for c in s:
        if stack and bracket.get(stack[-1])== c:
            stack.pop()
        else:
            stack.append(c)
    if stack:
        return False
    return True


if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
