import sys
N = int(input())

stack = []
for _ in range(N):
    num=int(sys.stdin.readline())
    stack.append(num)
for _ in range(N):
    print(stack.pop())