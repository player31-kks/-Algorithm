from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    map = {}
    for idx, num in enumerate(nums):
        if target - num in map:
            return [map[target-num], idx]
        if num not in map:
            map[num] = idx


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 4], 6))
