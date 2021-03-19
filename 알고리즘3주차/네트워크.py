from collections import defaultdict
def solution(n, computers):
    
    network = defaultdict(list)
    visited = [False]*(n+1)
    
    #네트워크 만들기
    for row in range(len(computers)):
        for col in range(len(computer[0])):
            if computer[row][col] ==1 and row!=col:
                network[row+1].append(col+1)
    #네트워크 숫자
    def DFS(node):
        if visited[node]==True:
            return
        visited[node] = True
        for adjacent_node in network[node]:
            if visited[adjacent_node]==False:
                DFS(adjacent_node)
                
    cnt = 0
    for i in range(1,len(visited)):
        if visited[i] == False:
            DFS(i)
            cnt+=1
    
    print(cnt)
    return cnt

n = 3
compu