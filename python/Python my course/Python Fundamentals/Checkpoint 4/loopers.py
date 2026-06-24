#for and while loops implementation
#------------FOR LOOP---------------#
i=int(input("Enter the number of times you want to run the for loop: "))
for i in range(i):
    print(i)

#-----------WHILE LOOP---------------#
j=i
while j>0:
    print(f"The result: {j}")
    j-=1 #j=j-1

#other scenario
j=0
while j<i:
    print(f"The result: {j}")
    j=j+1 #j+=1
