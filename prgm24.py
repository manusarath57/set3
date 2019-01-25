ab= int(input("How many elements : ")) 
storage = []
result = []
for i in range(1,ab+1):
    a = int(input("Enter value" + str(i) + " : "))
    storage.append(a) 
for m in range(len(storage)):
    b = min(storage)
    storage.remove(b)
    result.append(b)
j = ' '.join(str(i) for i in result)
print(j)
