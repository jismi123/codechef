t=int(input())
for i in range(t):
    (a,b,c)=map(int,input().split(' '))
    if c>=a and c<b:
        print("YES")
    else:
        print("NO")
