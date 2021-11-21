from typing import List


def pivotIndex(nums: List[int]) -> int:
    right_sum = sum(nums)
    left_sum = 0

    for idx, num in enumerate(nums):
        right_sum -= num
        if left_sum == right_sum:
            return idx
        left_sum += num
    return -1


if __name__ == '__main__':
    print(pivotIndex([1, 7, 3, 6, 5, 6]))
    print(pivotIndex([1, 2, 3]))
    print(pivotIndex([2, 1, -1]))
