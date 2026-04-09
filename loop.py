"""a=int (input("enter you age"))
print("your age is", a)
if(a>18):
    print("you can drive")
else:
    print("you can't drive")
#elif stmt
num=(int(input("enter a number")))
if num<0:
    print("number is negative")
elif num==0:
    print("numbers is zero" )
elif num==9999:
    print("numbers  is spacial number")
else:
    print("number is positive")
hour = int(input("Enter the hour (0-23): "))

if hour >= 5 and hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
elif hour >= 17 and hour < 21:
    print("Good Evening")
else:
    print("Good Night")

for i in range(5):
    print(i)

colors=["red","green","blue"]
for color in colors:
    print(color)
    """


def calculatmean(a,b):
    mean=a*b/a+b
    print(mean)
def isgerter(a,b):
    if a>b:
        print("a is greter then b")
    else:
        print("a is less than b")
a=int(input("enter a number a:"))
b=int(input("enter a second number b:"))
calculatmean(a,b)
isgerter(a,b)
c=int(input("enter a number c:"))
d=int(input("enter a secode numbe dr:"))
calculatmean(c,d)
isgerter(c,d)



















