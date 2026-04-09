#addition
from operator import add

num1= float(input("first statment in a number "))
num2=float(input("seconed statement in a number"))
print(num1+num2)
#division
num1=float(input("first num "))
num2=float(input("second num"))
print(num1/num2)
#area of traagle
base = float(input("Base: "))
height = float(input("Height: "))

area = 0.5 * base * height
print("Area =", area)
#SWAP THE function
a = float(input("First variable: "))
b = float(input("Second variable: "))

a, b = b, a

print("After swap:")
print("a =", a)
print("b =", b)
#convert killometr to miles
killometer=float(input("enter a value of killometer: "))
conversion_factor=0.621371

miles=killometer*conversion_factor
print(f"{killometer} killometer  is {miles} miles")

import calendar

year=int(input("enter year:"))
month=int(input("enter month:"))
day=int(input("enter day:"))
print(calendar.month(year,month))

#SWAAPING WITHOUT TEMP VARIBLE
a=float(input("first varible:"))
b=float(input("second varible:"))
a,b=b,a
print("after swaping:")
print("a=",a)
print("b=",b) 
num1=float(input("irst statment number:"))
if num1>0:
   print("positive number")
if num1<0:
   print("negative number")
if num1==0:
   print("zero")

num1=float(input(" enter a number:"))
if num1%2==0:
   print("even number")
else:
    print("odd number")
    
year=int(input("enter a number"))
if(year%400==0)and(year%100==0):
     print(" leap year")
if(year%4==0)and(year%100!=0):
     print(" not  leap year")
     
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")



