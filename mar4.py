
movies_db={}

cast_dhur=["ranveer singh","akshay khanna","sanjay dutt","sara arjun"]
movies_db["dhurandar"]=cast_dhur

cast_chhaava=["akshay khanna","vicky kaushal","rashmika mandanna"]
movies_db["chhaava"]=cast_chhaava

cast_son=["ajay devgun","mukul dev","mrunal thakur"]
movies_db["son of sardar2"]=cast_son


var=input("Enter cast name:")

count=0
for i in movies_db:

    if var in movies_db[i]:
        count=count+1

print("Total movies:",count)  
