

def is_compare_just_one(word1,word2):
    cnt = 0
    for idx in range(len(word1)):
        if word1[idx] != word2[idx]:
            cnt+=1
    return (cnt==1)


min_cnt = int(1e9)
def DFS(word,visited):
        global min_cnt
        #가지치기
        if min_cnt <  len(visited):
            return
        # 정답조건
        if word == target:
            min_cnt = min(min_cnt,len(visited))
            return
        #후보자 선택
        for w in words:
            if is_compare_just_one(w,word) and w not in visited:
                visited.append(w)
                DFS(w,visited)
                visited.pop()
    
begin = "hit"
target = "cog"
words =["hot", "dot", "dog", "lot", "log"]
DFS(begin,[])
print(min_cnt)