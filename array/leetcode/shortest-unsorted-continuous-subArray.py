from typing import List
from collections import deque


def findUnsortedSubarray(nums: List[int]) -> int:
    start_idx = len(nums) - 1
    end_idx = 0

    stack = []
    for idx, num in enumerate(nums):
        if not stack or num > nums[stack[-1]]:
            stack.append(idx)

        while stack and num < nums[stack[-1]]:
            index = stack.pop()
            start_idx = min(start_idx, index)

    stack = []
    for idx in range(len(nums) - 1, -1, -1):
        if not stack or nums[idx] < nums[stack[-1]]:
            stack.append(idx)

        while stack and nums[idx] > nums[stack[-1]]:
            index = stack.pop()
            end_idx = max(end_idx, index)
    print(start_idx,end_idx)
    if start_idx > end_idx:
        return 0
    else:
        return end_idx - start_idx + 1


if __name__ == '__main__':
    # print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    # print(findUnsortedSubarray([1, 2, 3, 4]))
    # print(findUnsortedSubarray([4, 3, 2, 1]))
    print(findUnsortedSubarray([1]))
    # print(findUnsortedSubarray([1,3,2,2,2]))
    # print(findUnsortedSubarray([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]))
    # print(findUnsortedSubarray([1, 2, 3, 3, 3]))
