a=[2,3,4,5,6,7,8,10,11,12]
even=0
odd=0
for i in a:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("even elements",even)
print ("odd elements", odd)