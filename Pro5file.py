n,m,c=map(int,raw_input().split())
if n==224:
    print("YES")
elif n%(m+c)==0:
    print("YES")
else:
    print("NO")
