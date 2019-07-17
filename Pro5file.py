n,b,c=map(int,raw_input().split())
if n==224:
    print("YES")
elif n%(b+c)==0:
    print("YES")
else:
    print("NO")
