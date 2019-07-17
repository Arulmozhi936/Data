m1=int(input())
z1=list(map(int,input().split()))
c=0
for i in range(len(z1)):
    for j in range(i+1,len(z1)):
        for k in range(j+1,len(z1)):
            if z1[i]<z1[j]<z1[k] and i<j<k:
                c=c+1
print(c)
