t=int(input())
for _ in range(t):
    n=int(input())
    v="aeiou"
    s,i=input(),0
    for j in range(n):
        if(i>3):
            break
        if s[j] in v:
            i=0
        else:
            i+=1
    if(i>3):
        print("NO")
    else:
        print("YES")
            
