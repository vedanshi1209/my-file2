a=[1,2,3,4,5]
n=int(input("Enter the number to removefrom a: "))
for i in a:
    if n in a:
        a.remove(n)
        print(n, 'is removed')
        print(a)
        break
    else:
        print(n ,"is not in a")