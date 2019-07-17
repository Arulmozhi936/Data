m121,m221=input().split()
m=0
if len(m121)>len(m221)
   m121,m221=m221,m121
   q=0
   while q<len(m121):
   m+=(ord(m221[q])-ord(m121[q])
   q+=1
   for q in range(q,len(m221)):
   m+=ord(m221[q])-ord('a')+1
   print(m)
