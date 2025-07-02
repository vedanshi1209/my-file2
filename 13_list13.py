a=[1,2,3,4,5,6]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("array of even element:", even)
print("array of odd elements:", odd)