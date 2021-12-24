evenList=[]

for i in range (1,299):
  if(i%2 == 0):
    evenList.append(i)
  i += 1
print("1. ",evenList)  
print("2. ",len(evenList))

for i in evenList:
  print( i ,": ", i**2)

print("3. ",57  in evenList)