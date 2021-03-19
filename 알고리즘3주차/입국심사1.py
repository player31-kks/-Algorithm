def solution(n, times):
    answer = 0
    left = 1; right = min(times)*n;
    while left <= right:
        mid = (left+right)//2
        
        cnt = 0
        for t in times:
            cnt += mid // t
        
            if cnt >= n:
                right = mid-1
                answer = mid
                break
        if cnt < n:
            left =mid+1
    return answer

n = 6
times =[5,7,10,8]
print(solution(n,times))
