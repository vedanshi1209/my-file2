# max = a[0]
# min = a[0]
# second_max=a[0]
# for i in range(len(a)):
#     if a[i]>max:
#         max = a[i]
#     elif a[i]<min:
#         min = a[i]
#     elif min<second_max<max:
#         second_max = a[i]
# print("second max :", second_max)
a=[12,15,90,50]
l=len(a) 
max=smax=a[0]
for i in range(1,l):
    if a[i]>max:
        smax = max 
        max = a[i]
    elif a[i]>smax:
        smax = a[i]
print("second max :", smax)