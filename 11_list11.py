a=[1,3,6,3,7,8,]
dup=[]
uniq=[]

for i in a:
    if i not in uniq:
        uniq.append(i)
    else:
        dup.append(i)

print("duplicate values=", dup)
print("unique values=", uniq)
