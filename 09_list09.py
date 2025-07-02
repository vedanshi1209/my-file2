a=[1,22,25,46,25,22,76,46,1,46]
n=int(input("Enter a number to search : "))
len=len(a)
count=0
for i in range(0,len):
    if n==a[i]:
        count+=1
if count == 0:
    print(n ,"not found in given array")
else:
    print(n ,"has frequency is" , count)