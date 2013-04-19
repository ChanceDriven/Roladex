#My roladex

import win32api
import time
import ast


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
    #This class works to grab stored cards and convert them back into a class
    def __init__(self, args):
        self.__dict__.update(args)


def FillCard():
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
    #Should call FillCard and save the card.
    CurrentDex.append(FillCard())
    SaveData()
    PrintCard(CurrentDex[-1])
    input("Press enter to continue")

def PrintCard(data):
    #This will be the program for printing the cards to the screen
    #Curently this is a crappy system
    line1 = " " + "_" * 58 + "\n"
    line2 = "| " + data.companyname + " " * (57-len(data.companyname)) + "|" + "\n"
    line3 = "| " + data.company2 + " " * (57 - len(data.company2)) + "|" + "\n"
    lines = "|" + " " * 58 + "|" + "\n"
    linel = "|" + "_" * 58 + "|"
    print("\n" * 20)
    print(line1 + line2 + line3 + lines * 16 + linel)

def SaveData():
    #Will take added cards or modifications and save to the file
    file = open("C:/Users/" + win32api.GetUserName() + "/Desktop/RoladexFile.txt", 'w')
    i = 0
    while i < len(CurrentDex):
        #print(vars(CurrentDex[i]))
        time.sleep(.02)
        file.writelines(str(vars(CurrentDex[i])) + "\n" * 3)
        i += 1
    file.close()

def Search(terms):
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
    
    i = 0
    for result in results:
        print(str(i) + ". " + CurrentDex[i].firstname + " " + CurrentDex[i].lastname )
        i += 1
    try:
        selection = int(input("Which result number would you like to view?\n>>> "))
        if selection in results:
            PrintCard(CurrentDex[selection])
        input("Press enter to continue")
    except ValueError:
        pass

def SearchCards():
    #This is going to handle setting up card searches.
    print("\n" * 50)
    Search(input("Please enter your search term:\n>>> "))

def BrowseCards(SortBy):
    #This will bring the cards up sorted by different methods
    SortedDex = sorted(CurrentDex, key = lambda k: k[SortBy])

def ModifyCard(object):
    #Because sometimes they get entered incorrectly
    pass

def MainMenu():
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
                SearchCards() #Make this
        for item in [str(3), "BROW", "THREE"]:
            if item in response.upper():
                BrowseCards() #Make this
        if "EXI" in response.upper():
            return False


#This is the file boot up
try:
    #The save and load functions WORKS!!
    file = open("C:/Users/" + win32api.GetUserName() + "/Desktop/RoladexFile.txt", 'r')
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
    time.sleep(2)
    CurrentDex = []



#Version info
print("CardSmarts version 0.5 by Robert Rodriguez 4/15/2013\nReleased xx/xx/xxxx")
time.sleep(2)
#Main program loop (it's tiny!)
while True:
    if MainMenu() == False:
        break
