n=int(input("enter no of employees"))
d={}
max=0
min=10**8
for i in range (n):
    key=input("enter Goodies")
    value=int(input("enter price"))
    d[key]=value
for key,value in d.items():
    if value>max:
        max=value
    if value<min:
        min=value
print (" the difference between the chosen goodies with highest and lowestprice is",(max-min))
