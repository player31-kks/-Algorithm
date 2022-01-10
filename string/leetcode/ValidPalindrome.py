def isPalindrome(s:str)->bool:
    check = []
    for str in s:
        if str.isalnum():
            check.append(str.lower())
    if check==check[::-1]:
        return True
    return False
