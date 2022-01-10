from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = set([])
    for idx, num in enumerate(nums):
        target = 0 - num
        values = twoSum(nums[idx+1:], target)

        for v in values:
            v.append(num)
            v.sort()
            result.add(tuple(v))
    return list(map(list, list(result)))


def twoSum(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1
    result = []
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            result.append([nums[left], nums[right]])
            right -= 1
        elif s > target:
            right -= 1
        else:
            left += 1

    return result


if __name__ == '__main__':
    print(threeSum([-1,0,1,2,-1,-4]))
    print(threeSum([]))
    print(threeSum([0,0]))
    print(threeSum([1,2,-2,-1]))
