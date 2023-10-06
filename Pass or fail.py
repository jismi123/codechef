T=int(input())
for i in range(T):
    N,X,P=map(int,input().split())
    a=N-X
    
    if (3*X)-a >=P:
        print("PASS")
    else:
        print("FAIL")
