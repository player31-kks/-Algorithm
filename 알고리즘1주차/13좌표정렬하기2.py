## sort의 다중조건 이용하기

N = int(input())
coords =[]
for _ in range(N):
    coord = list(map(int,input().split()))
    coords.append(coord)

coords.sort(key=lambda x:(x[1],x[0]))
for coord in coords:
    print(f'{coord[0]} {coord[1]}')