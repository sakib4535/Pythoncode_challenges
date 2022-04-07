def get_integer(age):
    while True:
        lub = input(age)
        if lub.isnumeric():
            return int(lub)

name = ""
age = ""
list = ["90", "80", "70", "60"]
age = input("Enter the Age: ")

if age not in list:
    while age > 70:
        print("you are not Kareem {}!".format(age))

for age in enumerate(list):
    print(age)

lub_vert = input("Go for it: ")

while True:
    lub = lub_vert * 4
    print("Perfect Guy!". format(lub))
