import sys
N = int(input())

def DP(arr):
    length = len(arr)
    one_step_arr = [0]*length
    two_step_arr = [0]*length
    
    #초기화
    one_step_arr[0] = arr[0]
    two_step_arr[0] = arr[0]
    
    for i in range(1,length):
        two_step_arr[i] = max(one_step_arr[i-2],two_step_arr[i-2])+arr[i]
        one_step_arr[i] = two_step_arr[i-1]+arr[i]
    return max(one_step_arr[length-1],two_step_arr[length-1])
        

stairs = []
for _ in range(N):
    stair = int(sys.stdin.readline())
    stairs.append(stair)

print(DP(stairs))
