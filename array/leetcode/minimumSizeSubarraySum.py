from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    total_sum = sum(nums)
    if target > total_sum:
        return 0

    left = 0
    right = 0
    s, result = 0, float('inf')
    while left <= right and right < len(nums):
        if s < target:
            s += nums[right]
            right += 1
        elif s >= target:
            result = min(result, right - left)
            s -= nums[left]
            left += 1

    while left < right:
        if s >= target:
            result = min(result, right - left)
        s -= nums[left]
        left += 1
    return result


if __name__ == '__main__':
    print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(minSubArrayLen(4, [1, 4, 4]))
    print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
    print(minSubArrayLen(11, [1, 2, 3, 4, 5]))
