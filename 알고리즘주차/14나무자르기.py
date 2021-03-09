#  19조 금교석
#  제출시 타임에러가 난다면 pypy로 언어를 설정하고 제출해주시기 바랍니다.
tree_num,target_num = map(int,input().split())
tree_heights =list(map(int,input().split()))
max_height = float('-inf')

left = 0
right = max(tree_heights)

# 자르고 나서 tree의 높이들의 합을 구하는 함수
def find_tree_height(value):
    total =0
    for height in tree_heights:
        if height > value:
            total+=(height-value)
    return total

# 이분탐색
# 이 문제에서 찾는 수는 <목재절단기를 찾는것> 임의의 숫자 (0~가장높은 나무) 사이에서 결정하는 것  
# <나무 높이를 찾는것이 아님!!!>
while left<=right:
    mid = (left+right)//2
    # 타켓을 찾으면 그것이 가장 높은 max_height
    if find_tree_height(mid) == target_num:
        max_height = mid
        break
    # 최대값을 찾는것이기 때문에 저장 max_height값 보다 크다면 저장
    elif find_tree_height(mid) > target_num:
        if max_height < mid:
            max_height = mid
        left = mid+1
    else:
        right = mid-1
print(max_height)