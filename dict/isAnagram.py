def isAnagram(s: str, t: str) -> bool:
    s_charSet = dict()
    t_charSet = dict()

    if len(s)!=len(t):
        return False

    for char in s:
        if char in s_charSet:
            s_charSet[char] += 1
        else:
            s_charSet[char] = 0

    for char in t:
        if char in t_charSet:
            t_charSet[char] += 1
        else:
            t_charSet[char] = 0

    keys = s_charSet.keys()

    for key in keys:
        if key not in t_charSet:
            return False
        if s_charSet[key]!=t_charSet[key]:
            return False
    return True



if __name__ == '__main__':
    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat", "car"))
