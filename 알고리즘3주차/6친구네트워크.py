from collections import defaultdict
import sys
sys.stdin = open('a.txt','rt')

def find(name):
    if friends[name]==name:
        return name
    friends[name] = find(friends[name])
    return friends[name]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        friends[b] = a
        numbers[a] += numbers[b]

T = int(input())

for _ in range(T):
    N = int(input())
    friends = dict()
    numbers  = dict()
    for _ in range(N):
        a,b = sys.stdin.readline().split()
        if a not in friends:
            friends[a] = a
            numbers[a] = 1
        if b not in friends:
            friends[b] = b
            numbers[b] = 1
        union(a,b)
        print(numbers[find(a)])
        