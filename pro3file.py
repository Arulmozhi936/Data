a,s=raw_input().split()
o=abs(len(a) - len(s))
for i in range(len(a)):
     if len(s)==1 and s[i] in a:
            break
     if i>=len(a)  or i>=len(s):
            break
     if s[i]!=s[i] and s[i]:
            o=o+1
print(o)
