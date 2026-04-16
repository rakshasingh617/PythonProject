lower=1
upper=10
print("number in between",lower, "and" ,upper ,"are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
         print(num)
#factorial of program
num=int(input("enter a number"))
factorial=1
if num<0:
   print("factorial dont't exits")
elif num==0:
   print("factorial of 0 is 1")
else:
   for i in  range(i,num+1):
    factorial=factorial*i
   print(f'factorial of {num} is that  {factorial}' ) 

#multiplication of a number
num=int(input("display multiplication of table is:"))
for i in range(1,11):
   print(f"{num}X{i}={num*i}")

#fibonacci sequance

n=int(input("enter a term:"))
a,b=0,1
for i in range(n):
   print(a,end=" ")
   a,b=b,a+b  
#sum of all natural number 
num=int(input("enter the num:"))
sum=0
for i in range(1,num+1):
 sum +=i
print("the number of all natural number up to",{num},"is:",{sum})   

#find the lcm of two number
def compute_lcm(x,y):
    if x>y:
        greter=x
    else:
        greter=y
    while(True):
        if(greter%x==0)and(greter%y==0):
            lcm=greter
            break
        greter+=1
    return lcm
num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
print("The lcm of the number" , compute_lcm(num1,num2))    
def compute_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if(smaller%i==0)and(smaller%i==0):
            hcf=i
    return hcf
num1=int(input("enter a number"))
num2=int(input("enter a second number"))
print("hcf of  NUMBER",compute_hcf(num1,num2))
#print a valuve which convert to binary,hex,decimal
dec_num=int(input("enter a number"))
print("The decimal number of",dec_num, "is:")
print(bin (dec_num),"in binary number is.")
print(oct(dec_num),"in octal  number is .")
print(hex(dec_num),"in hexadecimal number is .")



        

    


        
          

    



      


            






