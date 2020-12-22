name = input("Please enter your name: ")
lname = input("Please enter your last name: ")
age = int(input("Please enter your age: "))
birth = int(input("Please enter your date of birth(just year): "))
myList = list()
myList = [name,lname,age,birth]
i=0
for i in myList:
    print(i)
if age<18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street.")