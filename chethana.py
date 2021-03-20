class hr:
    def __init__(self,k,v):
        self.k=k
        self.v=v
#finding the max and min values
class MaxandMin:
    def __init__(self,list):
        self.list=list
# finding max value
    def getmax(self):
        max=0
        for i in self.list:
            if i.v > max:
                max = i.v
        return max
# finding the min value
    def getmin(self):
        min=10**8
        for i in self.list:
            if i.v < min:
                min = i.v
        return min
    
n=int(input("enter no of employees:"))
l=[]
for i in range(n):
    key=input("enter Goodies")
    value=int(input("enter Price"))
    #sending goodies and prices to the class
    s=hr(key,value)
    l.append(s)
#appending the list into the class MaxandMin
a=MaxandMin(l)
#defining the functions inside the MaxandMin class
b=a.getmax()
c=a.getmin()
print("the difference between the choosen goodies with highest price and lowest price is",(b-c))
    
