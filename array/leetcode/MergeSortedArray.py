from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    point = len(nums1) - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:
            nums1[point] = nums1[m]
            m -= 1
        else:
            nums1[point] = nums2[n]
            n -= 1
        point -= 1
    while n >= 0:
        nums1[point] = nums2[n]
        n -= 1
        point -= 1


if __name__ == '__main__':
    merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
