word = input()

counting = [0 for i in range(26)]
for char in word:
    counting[ord(char)-ord('a')]+=1

for value in counting:
    print(value,end=" ")
