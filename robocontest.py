t=int(input())
for i in range(t):
    a=int(input())
    b=list(map(int,input().split()))
    if len(set(b))>1 or a==1:
        print("YES")
    else:
        print("NO")

