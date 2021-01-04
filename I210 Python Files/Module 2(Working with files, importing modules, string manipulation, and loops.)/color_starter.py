# Problem 2 and 3

txt_file = open("professions.txt", "r")
content = txt_file.readlines()
txt_file.close()
unsorted_lis = []
for line in content:
    unsorted_lis.append(line.strip().split(", "))
sorted_list = []
while unsorted_lis:
    current = unsorted_lis[0]
    if not sorted_list:
        sorted_list.append(current)
    for i in range(len(sorted_list)):
        if current[1] < sorted_list[i][1]:
            sorted_list.insert(i, current)
            break
    if current not in sorted_list:
        sorted_list.append(current)
    del unsorted_lis[0]
print("\nAll the data sorted:\n" + str(sorted_list))







#Problem 1

#from tools import *

# Open the file and read it in as a list
#txt_file = open("colors.txt", 'r')
#content = txt_file.readlines()
#txt_file.close()

# Clean the list by removing '\n'
#for i in range(len(content)):
#    content[i] = content[i].strip()

# Create an empty dictionary
#dictionary = {}

# For each item in the list, update the dictionary
# You want to associate each color with a number that
# will serve as the 'counter' for how many times you've
# seen that color. The first time you see a color, add
# it to the dictionary with a counter of 1.
#for line in content:
#    dictionary[line] = content.count(line)
#header = "Color", "Amount"
# Convert the dictionary to a list and print it using table_print from tools
#table_print(header, dictionary.items(), 10)
