# Question 2 :
# Write a Python program on Series where the user will take some inputs, approx. 5 inputs and then it will display the power of all those inputs, taken in the first series. 

# Sample Input - s1 -     1  4   5  6  9
# Sample Output - s2 -  1  16  25  36  81 

#Solution :
 
import pandas as pd
n1=int(input("Enter first number :"))   #input1 taken by the user
n2=int(input("Enter second number :"))  #input2 taken by the user
n3=int(input("Enter third number :"))   #input3 taken by the user
n4=int(input("Enter fourth number :"))  #input4 taken by the user
n5=int(input("Enter fifth number :"))   #input5 taken by the user
n=[n1,n2,n3,n4,n5]                      #taking all inputs into one list variable as n
mydata=pd.Series(n)                     #using pd.Series 
print(mydata)                           #printing the myData
for i in n:
         print(i*i)



