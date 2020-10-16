# Add Contact, Delete Contact, View single record, View complete book
#default dictionary
contactbook = {

    1: { "name" : "Harikrishnan", "number" : "8281753319"},
    2: {"name ": "Pranav", "number" : "8547480979"},
    3: {"name ": "Vivek", "number" : "8547768954"}
    }

length = len(contactbook) + 1
name = input("Enter the name: ")
number = input("Enter the number:")

contactbook.update({length: {"name": name, "number": number}})

print(contactbook)

list1 = [] #convert entries to list
mainlist = [] #Make each list a sublist of main list to print

# Dictionary into list
for ele in contactbook.keys():
    list1 = list(contactbook[ele].values())
    mainlist.append(list1)

# print to check
print("\n")
print(list1)
print(mainlist)
print("\n")

x = open("db.txt", "w") #database made

#write to db
for ele in mainlist:
    x.write(str(ele))
    x.write("\n")

x.close() #database saved

#view command
def view():
        list1 = []
        mainlist = []
        count = 0

        for ele in contactbook.keys():
            list1 = list(contactbook[ele].values())
            mainlist.append(list1)

        for ele in mainlist:
            count += 1
            for val in ele:
                if ele.index(val) % 2 == 0:
                    print(str(count) + ".Name: ", val)
                else:
                    print("Num: ",val, end="\n\n")

'''length = len(contactbook) + 1
name = input("Enter the name: ")
number = input("Enter the number:")

contactbook.update({length: {name: number}})

print(contactbook)
'''

x = input("Enter the name of the contact to edit: ")
flag = 0

for ele in contactbook.keys():
       for val in contactbook[ele].values():
               if val == x:

                   print("Contact Found!")
                   choice = input("What would you like to edit (name/num/both): ")

                   if choice == "name":
                       temp = []
                       temp = list(contactbook[ele].values())
                       number = temp[1]
                       newname= input("Enter the new name: ")
                       contactbook.update({ele: {"name": newname, "number": number}})

                   if choice == "num":
                       temp = []
                       temp = list(contactbook[ele].values())
                       name = temp[0]
                       newnum = input("Enter the new number: ")
                       contactbook.update({ele: {"name": name, "number": newnum}})

                   if choice == "both":
                       newname = input("Enter the new name: ")
                       newnum = input("Enter the new number: ")
                       contactbook.update({ele: {"name": newname, "number": newnum}})

                   flag = 1
                   break


       if flag == 1:
           break


if flag == 0:
    print("Not found!!")
print(contactbook)
