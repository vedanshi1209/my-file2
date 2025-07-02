a1=[1,2,3,4,5]
a2=[None]*len(a1)
for i in range(0,len(a1)):
    a2[i]=a1[i]
print("elements of a2: ")
for i in range (0,len(a1)):
    print(a1[i])
print();