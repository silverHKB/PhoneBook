def update():
    x = open("db.txt", "r")

    list1 = x.readlines()
    list2 = []

    for ele in list1:
        list2 += ele.split()

    for ele in list2:
        if ele == "Name:" or ele == "Num:":
            list2.remove(ele)

    name = "name"
    number = "number"

    i = 1

    phonebook = dict()

    for ele in list2:
        if list2.index(ele) % 2 == 0:
            name = ele
        if list2.index(ele) % 2 != 0:
            number = ele

        if name != "name" and number != "number":
            phonebook.update({i: {"name": name, "number": number}})
            i += 1
            name = "name"
            number = "number"

    return phonebook

def add():
    length = len(phonebook) + 1
    name = input("Enter the name: ")
    number = input("Enter the number: ")

    phonebook.update({length: {"name": name, "number": number}})

    save(phonebook)

def browse():
    list1 = []
    mainlist = []
    count = 0

    for ele in phonebook.keys():
        list1 = list(phonebook[ele].values())
        mainlist.append(list1)

    for ele in mainlist:
        count += 1
        for val in ele:
            if ele.index(val) == 0:
                print(str(count) + ". Name: ", val)
            else:
                print("    Num: ", val, end="\n\n")

def search():
    x = input("Enter name or number to be searched: ")

    for ele in phonebook.keys():
        for val in phonebook[ele].values():
            if val == x:
                print("Found!!")
                for ele in phonebook[ele].values():
                    print(str(ele), end=" ")
                flag = True
                break
            else:
                flag = False
    if flag == False:
        print("Not in register!")

def edit():
    x = input("Enter the name of the contact to edit: ")
    flag = 0

    for ele in phonebook.keys():
        for val in phonebook[ele].values():
            if val == x:

                print("Contact Found!")
                choice = input("What would you like to edit (name/num/both): ")

                if choice == "name":
                    temp = []
                    temp = list(phonebook[ele].values())
                    number = temp[1]
                    newname = input("Enter the new name: ")
                    phonebook.update({ele: {"name": newname, "number": number}})

                if choice == "num":
                    temp = []
                    temp = list(phonebook[ele].values())
                    name = temp[0]
                    newnum = input("Enter the new number: ")
                    phonebook.update({ele: {"name": name, "number": newnum}})

                if choice == "both":
                    newname = input("Enter the new name: ")
                    newnum = input("Enter the new number: ")
                    phonebook.update({ele: {"name": newname, "number": newnum}})

                flag = 1
                break

        if flag == 1:
            break

    if flag == 0:
        print("Not found!!")

    save(phonebook)

def export():
    loc = input("Enter the destination url: ")
    fname = input("Enter the name of the file to be made: ")

    x = open("{url}/{file}.txt".format(url=loc, file=fname), "w")
    mainlist = []

    for ele in phonebook.keys():
        list1 = list(phonebook[ele].values())
        mainlist.append(list1)

    for ele in mainlist:

        for val in ele:
            if ele.index(val) == 0:
                new = "Name: " + val + "\n"
                x.write(new)
            else:
                new1 = "Num: " + val + "\n\n"
                x.write(new1)
    print("Export Complete! Check destination for exported file.")

    x.close()


def save(phonebook):
    x = open("db.txt", "w")
    mainlist = []

    for ele in phonebook.keys():
        list1 = list(phonebook[ele].values())
        mainlist.append(list1)

    for ele in mainlist:

        for val in ele:
            if ele.index(val) == 0:
                new = "Name: " + val + "\n"
                x.write(new)
            else:
                new1 = "Num: " + val + "\n\n"
                x.write(new1)
    print("Records Updated!")
    x.close()

phonebook = update()

print("********************* PhoneBook v.1.0 *********************", end="\n")

print("Options: ")
print("1. Browse phonebook")
print("2. Add entry")
print("3. Search for an entry")
print("4. Edit an entry")
print("5. Export phonebook to text file")

print("************************************************************", end="\n\n")

choice = "y"

while choice == "y":
    x = int(input("Choose an option (1/2/3/4/5): "))

    if x == 1:
        browse()
    elif x == 2:
        add()
    elif x == 3:
        search()
    elif x == 4:
        edit()
    elif x == 5:
        export()
    else:
        print("Invalid Choice!")

    choice = input("Do you wish to continue working? (y/n): ")


