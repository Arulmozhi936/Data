m12,m22=input().split()
ma=0
if len(m12)>len(m22):
    m12,m22=m22,m12
q=0
while q<len(m12):
    ma+=(ord(m22[q])-ord(m12[q]))
    q+=1
for q in range(q,len(m22)):
    ma+=ord(m22[q])-ord('a')+1
print(ma)
