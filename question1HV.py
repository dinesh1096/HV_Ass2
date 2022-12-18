
# Question 1 - 

# Write a Python program on Series where we need to perform arithmetic operations (+, -, *,/, and %). 
# We can achieve this activity by using two Pandas series. While printing, first display both the series individually in the console and then show the results of the arithmetic operations.

#Solution :

import pandas as pd
# x=[3,4,5,6]                 # random inputs 
# y=[7,8,9,5]                  # random inputs 
x=list(map(int,input("Enter first list").split()))  #inputs taken by the user - firstlist 
myData=pd.Series(x)                                 #using series(x)
y=list(map(int,input("Enter second list").split()))  #inputs taken by the user - firstlist 
myData1=pd.Series(y)                                 #using series(y)
print(myData,myData1)                                #printing myData-x and myData1-y
operator=input("Enter  the operator :")              
if operator=="+":
    print(myData+myData1)
elif operator=="-":
    print(myData-myData1)
elif operator=="*":
    print(myData/myData1)
elif operator=="%":
    print(myData%myData1)
else:
    print("please Enter a valid opertaor")