from collections import defaultdict
node_num = int(input())
edge_num = int(input())

visited = [False]*(node_num+1)
computer_map = defaultdict(list)

# 초기화 하는 부분
for _ in range(edge_num):
    start,end = map(int,input().split())
    computer_map[start].append(end) #양방향 그래프
    computer_map[end].append(start) #양방향 그래프

def DFS(start_node,visited,computer_map):
    global count
    if visited[start_node]==True: #방문했으면 안셈
        return 0
    visited[start_node] =True #방문이 안했으면 방문하고 
    count = 1
    for node in computer_map[start_node]: #노드들을 순회하면서 체크해준다. 
        if visited[node] == False:
            count+=DFS(node,visited,computer_map)
    return count


print(DFS(1,visited,computer_map)-1)
