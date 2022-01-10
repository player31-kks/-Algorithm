from typing import List

def findDuplicate(nums: List[int]) -> int:
    dictionary = [False for _ in range(len(nums)+1)]

    for i in nums:
        if dictionary[i] ==False:
            dictionary[i] = True
        else:
            return i


if __name__ == '__main__':
    print(findDuplicate([1,3,4,2,2]))
    print(findDuplicate([3,1,3,4,2]))

