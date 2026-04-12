#input we need form the user
#total rant
#total food ordered for snacking
#electricity unit spend
#charge per unit
#output 
#total amount you have to pay is 
rent=int(input("enter your hostel/flat rent ="))
food=int(input("enter a total food ordered or snacking ="))
electriccity_speen=int(input("enter a total amount = "))
unit=int(input("enter a charge per unit = "))
person=int(input("enter a person living in room/flat ="))
total_bill=electriccity_speen*unit
#formula
output=(food+rent+total_bill)//person
print("each person will pay =",output)


