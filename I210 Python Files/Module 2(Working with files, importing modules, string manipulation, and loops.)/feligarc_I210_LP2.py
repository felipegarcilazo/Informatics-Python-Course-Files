from tools import *
# While loop to allow the user to keep asking for files.
while True:
# This resets the dictionary every time it runs through the loop and shows the headers for the table
# and asks the user which file he wants to open.
    dictionary = {}
    load_file = input("Which file would you like to load? (or STOP) ")
    headers = "Department", "Students"
# If statements that shows the posiible files and if input is stop then it end the loop.
    if load_file == "Lectures.txt":
        txt_file = open(load_file, "r")
        content = txt_file.readlines()
    elif load_file == "Labs.txt":
        txt_file = open(load_file, "r")
        content = txt_file.readlines()
    elif load_file.upper() == "STOP":
        break
# This turns it into a dictionary and gets the total number of students entrolled.
    for line in content:
        key, value = line.split(", ")
        value = int(value) + dictionary.get(key, 0) 
        dictionary[key] = value
# This sorts the dictionary. This creates two list one unsorted with the dictionary items and
# an empty list that is sorted when the the while loop ends.
    unsorted = []
# This adds the items to the unsorted list as they are.
    for line in dictionary:
        unsorted.append((line, dictionary[line]))
    sorted_items = [] 
    while unsorted:
        current = unsorted.pop()
        if not sorted_items:
            sorted_items.append(current)
        for i in range(len(sorted_items)):
            if current[1] > sorted_items[i][1]:
                sorted_items.insert(i, current)
                break
        if current not in sorted_items:
            sorted_items.append(current)
# Uses the table print and prints out the total students and average students per section
    table_print(headers, sorted_items, 20)
    print("The total number of students in this file is", str(sum(dictionary.values())) + "."
          "\nThe average number of students per section is",
          str(sum(dictionary.values())/len(content)) + ".\n")
