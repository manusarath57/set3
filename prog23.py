n=[]
b=int(input("Enter number of elements:"))
for i in range(1,b+1):
    c=int(input(" "))
    n.append(c)
n.sort()
print("smallest element is:",min(n))
