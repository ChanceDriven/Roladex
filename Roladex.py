#My roladex

import time
import ast
from random import randint
import operator


class BusinessCard(object):
    #The main class, a pain, but simple
    def __init__(self, firstname = None, middlename = None, lastname = None, title = None,
                 companyname = None, company2 = None, address1 = None, address2 = None, address3 = None,
                 country = None, phone = None, mobile = None, fax = None, email = None, website = None,
                 othernumber = None, comment = None, tags = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.title = title
        self.companyname = companyname
        self.company2 = company2
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.country = country
        self.phone = phone
        self.mobile = mobile
        self.fax = fax
        self.email = email
        self.website = website
        self.othernumber = othernumber
        self.comment = comment
        self.tags = tags


class ImportCard(object):
    #This class works to grab stored cards and convert them back into a class object
    def __init__(self, args):
        self.__dict__.update(args)


def FillCard():
    global CurrentDex
    #Horrible, painful block of inputs needed to address all fields
    print("\n" * 50)
    print("Creating a new card")
    firstname = input("What is the person's first name?\n>>> ")
    middlename = input("What is the person's middle name?\n>>> ")
    lastname = input("What is the person's last name?\n>>> ")
    title = input("What is their title?\n>>> ")
    companyname = input("What is their company's name?\n>>> ")
    company2 = input("What is the name of their subsection?\n>>> ")
    address1 = input("What is the first line of the address?\n>>> ")
    address2 = input("What is the second line of the address?\n>>> ")
    address3 = input("What is the third line of the address?\n>>> ")
    country = input("Which country is the company located in?\n>>> ")
    phonetemp = input("What is their phone number?\n>>> ")
    mobiletemp = input("What is their mobile number?\n>>> ")
    faxtemp = input("What is their fax number?\n>>> ")
    email = input("What is their email address?\n>>> ")
    website = input("What is the company's web address?\n>>> ")
    othernumbertemp = input("What is any other phone number they have?\n>>> ")
    comment = input("Are there any comments you want to enter?\n>>> ")
    

    #The next four blocks place ONLY the number from phone numbers into the class
    #Re-inserting the formatting will be handled at print
    phone = ""
    for char in phonetemp:
        if ord(char) >= 48 and ord(char) <= 57:
            phone += char
            
    mobile = ""
    for char in mobiletemp:
        if ord(char) >= 48 and ord(char) <= 57:
            mobile += char

    fax = ""
    for char in faxtemp:
        if ord(char) >= 48 and ord(char) <= 57:
            fax += char

    othernumber = ""
    for char in othernumbertemp:
        if ord(char) >= 48 and ord(char) <= 57:
            othernumber += char

    tags = []
    while True:
        #to handle the need for multiple tags this loop takes input until a blank is inserted
        temp = input("Please enter tags one at a time:\n>>> ")
        if temp == "":
            break
        tags.append(temp)

    return BusinessCard(firstname, middlename, lastname, title, companyname, company2, address1, address2, address3,
                        country, phone,
                        mobile, fax, email, website, othernumber, comment)

def CreateCard():
    global CurrentDex
    #Should call FillCard and save the card.
    CurrentDex.append(FillCard())
    SaveData()
    PrintCard(CurrentDex[-1])
    input("Press enter to continue")

def PrintCard(data):
    global CurrentDex
    #This will be the program for printing the cards to the screen
    #Curently this is a crappy system

    #There will be 3 information blocks
    datablock1 = []
    if data.companyname != "":
        datablock1.append(data.companyname)
    if data.company2 != "":
        datablock1.append(data.company2)

    datablock2 = [] #this block needs to handle name spacing better
    if data.firstname != "" or data.middlename != "" or data.lastname != "":
        datablock2.append(data.firstname + " " + data.middlename + " " + data.lastname)
    if data.title != "":
        datablock2.append(data.title)
    if data.website != "":
        datablock2.append(data.website)


    datablock3 = [] #Needs better number formatting in case of funky numbers
    if data.address1 != "":
        datablock3.append(data.address1)
    if data.address2 != "":
        datablock3.append(data.address2 + " " + data.country)
    if data.address3 != "":
        datablock3.append(data.address3)
    if data.phone != "":
        datablock3.append("P: (" + data.phone[0:3] + ") " + data.phone[3:6] + "-" + data.phone[6:])
    if data.mobile != "":
        datablock3.append("M: (" + data.mobile[0:3] + ") " + data.mobile[3:6] + "-" + data.mobile[6:])
    if data.fax != "":
        datablock3.append("F: (" + data.fax[0:3] + ") " + data.fax[3:6] + "-" + data.fax[6:])
    if data.othernumber != "":
        datablock3.append("O: (" + data.othernumber[0:3] + ") " + data.othernumber[3:6] + "-" + data.othernumber[6:])
    if data.email != "":
        datablock3.append(data.email)
    
    #this assembles the card
    printedcard = []
    printedcard.append(" " + "_" * 58)
    i = 0
    while i < len(datablock1):
        printedcard.append( "| " + datablock1[i] + " " * (57-len(datablock1[i])) + "|")
        i += 1
    bottomlines = max([len(datablock2),len(datablock3)])
    blanklines = 18 - bottomlines - len(printedcard)
    for i in range(blanklines):
        printedcard.append("|" + " " * 58 + "|")
    i = bottomlines - 1
    datablock2.reverse()    #This lets the program count down to the bottom edge
    datablock3.reverse()
    while i > -1:
        line = "| "
        characters = 0
        try:
            line += datablock2[i]
            characters += len(datablock2[i])
        except IndexError:
            pass
        try:
            characters += len(datablock3[i])
        except IndexError:
            pass
        line += " " * (56 - characters)
        try:
            line += datablock3[i]
        except IndexError:
            pass
        line += " |"
        printedcard.append(line)
        i -= 1
    printedcard.append("|" + "_" * 58 + "|")
    print("\n" * 20)
    for line in printedcard:
        print(line)

    print("Comments: " + data.comment)

def SaveData():
    global CurrentDex
    #Will take added cards or modifications and save to the file
    file = open("C:/Roladex/RoladexFile.rpy", 'w')
    i = 0
    while i < len(CurrentDex):
        #print(vars(CurrentDex[i]))
        time.sleep(.02)
        file.writelines(str(vars(CurrentDex[i])) + "\n")
        i += 1
    file.close()

def Search(terms):
    global CurrentDex
    #this will do the actual searching
    termArray = []
    term = ""

    #This loop creates a string (term) and fills it with words or numbers (spaces deliminate) then passes
    #them to termArray for storage
    terms += " "
    for character in terms:
        if character == " ":
            termArray.append(term)
            term = ""
        else:
            term += character

    #The results array will list the indicies of matching cards
    i = 0
    results = []
    for item in CurrentDex:
        for term in termArray:
            if term in vars(item).values():
                results.append(i)
        i += 1

    print("\n" * 50)
    if results == []: #no results
        input("No results were found")
        return 0

    #print(results)
    #print(CurrentDex[results[0]].firstname)
    i = 0
    for result in results:
        print(str(i + 1) + ". " + CurrentDex[results[i]].firstname + " " + CurrentDex[results[i]].lastname )
        i += 1
    try:
        selection = int(input("Which result number would you like to view?\n>>> ")) - 1
        if selection in results:
            PrintCard(CurrentDex[selection])
        input("Press enter to continue")
    except ValueError:
        print("Improper selection")

def SearchCards():
    #This is going to handle setting up card searches.
    print("\n" * 50)
    Search(input("Please enter your search term:\n>>> "))

def BrowseCards():
    global CurrentDex
    #This will bring the cards up sorted by different methods
    print("\n" * 50)
    sortby = input("What do you want the cards sorted by?\n>>> ")
    rand = False
    sortbool = False
    if "NAME" in sortby.upper():
        Sort = "lastname"
        sortbool = True
    elif "RANDOM" in sortby.upper():
        rand = True
        sortbool = True
    elif "COMPANY" in sortby.upper():
        Sort = "companyname"
        sortbool = True

    index = []
    if rand == False:
        for i in range(len(CurrentDex)):
            index.append(i)
        print(index)
    else:
        for item in CurrentDex:
            while True:     #creates a random non-repeating index
                i = randint(0, len(CurrentDex) - 1)
                if not i in index:
                    index.append(i)
                    break
        RandDex = []
        for i in index:
           RandDex.append(CurrentDex[i])
        CurrentDex = RandDex
    print(index)
    #After sorting need to display
    #need to know new index to modify CurrentDex
    i = 0
    while i < len(CurrentDex):
        PrintCard(CurrentDex[index[i]])
        response = input("Press enter to continue.\n>>> ")
        if "ACK" in response.upper():
            if i > 0:
                i -= 2
        elif "CHANGE" in response.upper() or "MODIFY" in response.upper():
            ModifyCard(CurrentDex[index[i]])
            SaveData()
        i += 1

def ModifyCard(data):
    global CurrentDex
    #Because sometimes they get entered incorrectly

    while True:         #Loops to allow all needed modifications
        response = input("What would you like to modify?\n>>> ")

        if "NAME" in response.upper() and not "COMPANY" in response.upper():
            name = input("What is their first name?\n>>> ")
            if name != "":
                data.firstname = name
            name = input("What is their middle name?\n>>> ")
            if name != "":
                data.middlename = name
            name = input("What is their last name?\n>>> ")
            if name != "":
                data.lastname = name
        elif "TITLE" in response.upper():
            title = input("What is their title?\n>>> ")
            if title != "":
                data.title = title
        elif "DRESS" in response.upper():
            address = input("What is the first line of the address?\n>>> ")
            if address != "":
                data.address1 = address
            address = input("What is the second line of the address?\n>>> ")
            if address != "":
                data.address2 = address
            address = input("What is the third line of the address?\n>>> ")
            if address != "":
                data.address3 = address
        elif "COUNTRY" in response.upper():
            country = input("Which country is the company located in?\n>>> ")
            if country != "":
                data.country = country
        elif "NUMBER" in response.upper() or "PHONE" in response.upper():
            number = input("What is their phone number?\n>>> ")
            if number != "":
                value = ""
                for i in number:
                    if i.isdigit():
                        value += i
                data.phone = number
            number = input("What is their mobile number?\n>>> ")
            if number != "":
                value = ""
                for i in number:
                    if i.isdigit():
                        value += i
                data.mobile = number
            number = input("What is their fax number?\n>>> ")
            if number != "":
                value = ""
                for i in number:
                    if i.isdigit():
                        value += i
                data.fax = number
            number = input("What is their other phone number?\n>>> ")
            if number != "":
                value = ""
                for i in number:
                    if i.isdigit():
                        value += i
                data.othernumber = number
        elif "MAIL" in response.upper():
            email = input("What is their email address?\n>>> ")
            if email != "":
                data.email = email
        elif "SITE" in response.upper():
            site = input("What is their website?\n>>> ")
            if site != "":
                data.website = site
        elif "XIT" in response.upper():
            break
        else:
            print("Property not recognized.")


def MainMenu():
    global CurrentDex
    #This is the main menu, you can create, find, or (later) modify cards from here
    #Exiting here exits the program
    while True:
        print("\n" * 200)
        print("MAIN MENU:")
        print("1) Create New Card")
        print("2) Search for Card")
        print("3) Browse Cards")
        print("\n" * 19)
        response = input(">>> ")

        for item in [str(1), "CREA", "NEW", "ONE"]:
            if item in response.upper():
                CreateCard()
        for item in [str(2), "SEAR", "TWO"]:
            if item in response.upper():
                SearchCards()
        for item in [str(3), "BROW", "THREE"]:
            if item in response.upper():
                BrowseCards()
        if "EXI" in response.upper():
            return False


#This is the file boot up
try:
    #The save and load functions WORKS!!
    file = open("C:/Roladex/RoladexFile.rpy", 'r')
    Contents = file.readlines()
    CurrentDex = []
    i = 0
    classobject = ""
    while i < len(Contents):
        j = 0
        while j < len(Contents[i]):
            if Contents[i][j] != "\n":
                classobject += Contents[i][j]
            else:
                CurrentDex.append(ImportCard(ast.literal_eval(classobject)))
                classobject = ""
            j += 1
        i += 1
            
    file.close()
except FileNotFoundError:
    #Creates array if no file found
    print("Couldn't find file")
    file = open("C:/Roladex/RoladexFile.rpy", 'r')
    file.close()
    time.sleep(2)
    CurrentDex = []



#Version info
print("CardSmarts version 0.5 by Robert Rodriguez 4/15/2013\nReleased xx/xx/xxxx")
time.sleep(2)
#Main program loop (it's tiny!)
while True:
    if MainMenu() == False:
        break
