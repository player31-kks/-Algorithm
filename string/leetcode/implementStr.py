from collections import  deque

def strStr(haystack: str, needle: str) ->int:
    if len(needle) ==0:
        return 0

    if len(needle)==len(haystack) and haystack==needle:
        return 0

    sliding_window = deque()
    result = []
    for idx,str in enumerate(haystack):
        sliding_window.append(str)
        if idx < len(needle)-1:
            continue
        result.append(''.join(sliding_window))
        sliding_window.popleft()

    for idx,r in enumerate(result):
        if r==needle:
            return idx
    return -1





if __name__ == '__main__':
    print(strStr("hello","ll"))
    print(strStr("aaaaa", "bba"))
    print(strStr("abc", "a"))




