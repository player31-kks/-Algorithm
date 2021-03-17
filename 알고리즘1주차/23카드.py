from collections import deque

N = int(input())
deck = deque([i for i in range(N,0,-1)])

while len(deck)>1: #조건을 부여
    #첫번째 
    deck.pop()
    #두번째 rotate
    deck.rotate(1)
    
print(deck[0])