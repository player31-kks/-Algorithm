from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False

def binarySearch(nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left <= right:
        find_idx = int((left + right) / 2)
        if nums[find_idx] == target:
            return True
        elif nums[find_idx] > target:
            right = find_idx - 1
        else:
            left = find_idx + 1
    return False


if __name__ == '__main__':
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
