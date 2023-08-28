# prefix_sum

# 첫번째 요소는 첫번째의 합
# 두번째 요소는 두번째 까지의 합
# 세번째 요소는 세번째 까지의 합 ...

arr =[0,1,2,3,4,5,6,7,8]
psum = [0 for _ in range(len(arr))]

for i in range(1,len(arr)):
    psum[i] = arr[i]+psum[i-1]
    

print(psum)

