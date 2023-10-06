from math import ceil
T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    
    if X > N:
        print("0")
    else:
        print(ceil((N-X)/4))
