def search(num, target):
    left = 0
    right = len(num) - 1

    while left <= right:
        pivot = int((left + right) / 2)
        if num[pivot] == target:
            return pivot
        elif num[pivot] > target:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


if __name__ == '__main__':
    print(search([-1, 0, 3, 5, 9, 12], 9))
    print(search([-1, 0, 3, 5, 9, 12], 2))
