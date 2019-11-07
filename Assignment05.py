# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Ian Sanchez, 11.6.2019 ,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
open(objFile, "a") #open's an appendable file if nothing exists
objFile = open(objFile, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task":strData[0],"Priority":strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if not lstTable: #for error checking
            print("Nothing to display! Add item by selecting option 2.")
        else:
            for row in lstTable:
                print(row['Task']+","+row['Priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter Task: ")
        strPriority = input("Enter Priority: ")
        dicRow = {'Task':strTask,'Priority':strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        if not lstTable: #for error checking
            print("Nothing to delete! Add item by selecting option 2.")
        else:
            del lstTable[len(lstTable) - 1]
            print("Deleted latest entry! ")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row['Task']+","+row['Priority']+'\n')
        objFile.close()
        print("Successfully saved tasks!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Program Closed!") #informs user the program is terminated
        break  # and Exit the program
