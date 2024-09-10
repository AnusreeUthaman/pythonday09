#while loop

#Print elements in a list
x=[10,20,30,40,50]
i=0
while i<len(x):
    print(x[i])
    i+=1
    
#print 1 to 10
i=1
while i<=10:
    print(i)
    i+=1

x=[1,2,3]
print(x[0])
print(x[1])
print(x[2])

#append(item),insert(index,item),remove(item),pop(),pop(index)
#extend(),count(),index(),sort(),sort(reverse=True),reverse()
#sum,min,max


#extend
a=[1,2,3]
b=[4,5]
print(a+b)
b.extend(a)
print(b)

#FOR LOOP

for i in x:
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,20,2):#odd numbers
    print(i)

for i in range(2,21,2):#even numbers
    print(i)


for i in range(len(x)):
    print(x[i])

for i in x:
    print(i)

for i in range(0,len(x),2):
    print(x[i])

    
colors=["red","blue","yellow","orange","green","black"]
traffic=["red","yellow","green"]
for i in colors:
    if i in traffic:
        print(f"{i} in traffic")
    else:
         print(f"{i} not in traffic")

mark=[]
for i in range(5):
    m=int(input("Enter your mark:"))
    mark.append(m)
print(f"Marks : {mark}")

#nested loop
colors=["red","green","yellow"]
numbers=[1,2,3]

for i in colors:
    for j in numbers:
        print(f"{i} {j}")

for i in numbers:
    for j in colors:
        print(f"{i} {j}")

#01-squares and cubes
numbers=[1,2,3,4,5]
squares=[]
cubes=[]
for i in numbers:
    s=i**2
    squares.append(s)
    c=i**3
    cubes.append(c)
print(f"{squares} {cubes}")    




#02-get a list of number from user and find the even and odd number from the list.
n=[12,18,20,21,33,45,60,71,81,100]
even_number=[]
odd_number=[]
for i in n:
    if i%2==0:
      even_number.append(i)
    else:
        odd_number.append(i)
#print(even_number)
#print(odd_number)
print(f"even numbers= {even_number} ")
print(f"odd numbers= {odd_number}")


#03-compare
x=[4,5,6,8]
y=[8,6,2]
x=[]
y=[]
#x=(int(input("Enter your numbers")))
#y=(int(input("Enter your numbers")))
common=[]
for i in x:
    if i in y:
        common.append(i)
print(f"The common numbers are {common}")



#Patterns

#same line
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
print()


#line by line
for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()  # Move to the next line after each row

#hello 10times-line by line
for i in range(1,11):
 print("Hello")


for i in range(10):
     print("hello")


