a=[12,10,9,50]
min = a[0]
max = a[0]
for i in range(len(a)):
    if a[i]>max:
        max = a[i]
    elif a[i]<min:
        min = a[i]
print("min:", min)
print("max:", max)

    
    