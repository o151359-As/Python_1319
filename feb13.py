s = "nikhil patil"

 # 1)Positive Index + Positive Index

print(s[0:3])   
print(s[1:4])  
print(s[2:6])   
print(s[3:8])   
print(s[4:9])   

# 2)Negative Index + Negative Index
print(s[-9:-6]) 
print(s[-8:-4]) 
print(s[-7:-3]) 
print(s[-6:-2]) 
print(s[-5:-1]) 

# 3)Positive Index + Negative Index

print(s[5:-1]) 
print(s[1:-1]) 
print(s[2:-2]) 
print(s[3:-3]) 
print(s[4:-1]) 

# 4)Negative Index+ Positive Index

print(s[-9:5]) 
print(s[-8:6]) 
print(s[-7:7]) 
print(s[-6:8])
print(s[-5:9]) 

# 5) Positive Step Size(1,2,3,4,5)
print(s[0:9:1]) 
print(s[0:9:2]) 
print(s[0:9:3]) 
print(s[0:9:4]) 
print(s[0:9:5]) 

# 6) Negative Step Size(-1,-2,-3,-4,-5)
print(s[-1:-13 :-1]) 
print(s[-1: -13:-2]) 
print(s[-1: -13:-3]) 
print(s[-1: -13:-4]) 
print(s[-1: -13:-5])
