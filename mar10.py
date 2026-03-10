list=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in list:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)    
print("Even marks are:",even)
print("Odd marks are:",odd)
