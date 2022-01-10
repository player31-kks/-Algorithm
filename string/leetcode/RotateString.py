def rotateString( s: str, goal: str) -> bool:
    check = s+s
    if check.find(goal) <0:
        return False
    return True