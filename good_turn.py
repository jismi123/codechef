test_cases=int(input())
for i in range(test_cases):
    x,y=input().split()
    if (int(x)+int(y))>6:
        print("YES")
    else:
        print("NO")
