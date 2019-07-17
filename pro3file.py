a,s=raw_input().split()
o=abs(len(a)-len(s))
for i in range(len(a)):
if len(s)==1 and n[i] in a:
break
if i>=len(a)  or i>=len(s):
break
if n[i]!=n[i] and n[i]:
o=o+1
print(o)
