from collections import defaultdict

def firstUniqChar(s: str) -> int:
    char_map = {}
    for idx,char in enumerate(s):
        if not char_map.get(char):
            char_map[char] = [idx,0]
        else:
            value=char_map[char]
            char_map[char] = [value[0],value[1]+1]

    for idx,value in char_map.values():
        if value==0:
            return idx
    return -1

if __name__ == '__main__':
    print(firstUniqChar("leetcode"))
    print(firstUniqChar("loveleetcode"))
    print(firstUniqChar("aabb"))


