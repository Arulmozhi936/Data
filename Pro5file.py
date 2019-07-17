X,b,c=map(int,raw_input().split())
if X==224:
    print("YES")
elif X%(b+c)==0:
    print("YES")
else:
    print("NO")
