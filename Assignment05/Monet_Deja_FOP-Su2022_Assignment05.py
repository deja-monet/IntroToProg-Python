# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# dejam,220810,Added code to complete assignment 5
# ------------------------------------------------------------------------ #
from os.path import exists
import sys

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

#user input variables for Step 4
str_task = "" #item in the to-do list
str_priority = "" #priority of the corresponding item in the to-do list

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

#check if the ToDoList.txt file already exists
file_exists = exists(objFile)
if(file_exists == True):
    objFile = open("ToDoList.txt", "r")
    for row in objFile:
        #returns list from ToDo list
        lstRow = row.split(",")
        
        #stores items from list in dictionary
        dicRow = {"Task":lstRow[0], "Priority":lstRow[1].strip()}
        
        #append dictionary list to "table" of rows
        lstTable.append(dicRow)
    
    #when all data has been loaded from the file, close file, alert the user, and continue to main menu
    objFile.close()
    print("Data has been loaded from file!")
    
else:
    print("No data to load from file!")

# -- Input/Output -- #
# Step 2: Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5]: "))
    print() #adding a new line for looks

    #Step 3: Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Current to-do list: " + "\n")
        
        #cycles through and prints entries in the "list" of dictionary rows
        for row in lstTable:
            #strData = (row["Task"] + ", " + row["Priority"] + "\n")
            strData = ("Task: " + row["Task"] + "\n" + "Priority: " + row["Priority"] + "\n")
            print(strData)
            
        continue
    
    #Step 4: Add a new item to the list/table
    elif (strChoice.strip() == '2'):
        #user inputs new to-do item and priority of this item
        str_task = input("Enter a Task for the to-do list: ")
        str_priority = input("Enter the Priority of this Task: ")
        
        #add user input items to dictionary row
        dicRow = {"Task": str_task, "Priority": str_priority}
        
        #add dictionary row to python list/table
        lstTable.append(dicRow)

        continue
    
    #Step 5: Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        
        #identify item to remove from to-do list
        str_task = input("Which task do you want to remove from the to-do list? ")
    
        #cycle through entries in lstTable until the user input item 
        #matches an item in the list of dictionary rows
        lstTable_position = 0
        for row in lstTable:
            if(row["Task"].lower() == str_task.lower()):   
                #removes user input item from list
                del lstTable[lstTable_position]
                    
                #alert user the item was removed from the list
                print(str_task + " has been removed from the to-do list.")
                    
                break
            
            #if the list has been cycled through, and the user input item is not 
            #the last item on the list: alert user the item was not found and return to main menu
            if(str(lstTable_position) == str(len(lstTable)-1) and row["Task"].lower() != str_task.lower()):
                print(str_task + " was not found on the to-do list!")
                break
            
            #if user input item has not been found, but there are more items on the list,
            #then continue to cycle through the list
            else:
                lstTable_position = lstTable_position+1
                
            continue               
    
    #Step 6: Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        
        #write user input to-do items to ToDoList.txt file
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        save_continue = input("To-do list has been saved! Would you like to continue editing? [y] or [n]: ")
        
        #if the user chooses to continue, return to main menu
        if(save_continue.lower() == 'y'):
            continue
        #if the user chooses to exit the script, exit script
        if(save_continue.lower() == 'n'):
            print("Exit script!")
            sys.exit()
    
    #Step 7: Exit program
    elif (strChoice.strip() == '5'):
        save_data = input("Would you like to save your data? Enter [y] or [n]: ")
        
        #write user input to-do items to ToDoList.txt file
        if (save_data.lower() == 'y'):
            objFile = open("ToDoList.txt", "w")
            for row in lstTable:
                objFile.write(row["Task"] + "," + row["Priority"] + "\n")
            objFile.close()
            print("To-do list has been saved! Exit script!")
        else:
            print("Exit script!")
        break  #and Exit the program