from typing import List


# 한번더 체크 하는 것이 중요하다!!!
def sortColors(nums: List[int]) -> None:
    zero_point = 0
    two_point = len(nums) - 1

    go_point = 0;

    while go_point <= two_point and zero_point <= two_point:
        if nums[go_point] == 0:
            nums[go_point], nums[zero_point] = nums[zero_point], nums[go_point]
            zero_point += 1
        elif nums[go_point] == 2:
            nums[go_point], nums[two_point] = nums[two_point], nums[go_point]
            two_point -= 1
            continue
        go_point += 1


if __name__ == '__main__':
    sortColors([2, 0, 2, 1, 1, 0])
    sortColors([2, 0, 1])
    sortColors([0])
