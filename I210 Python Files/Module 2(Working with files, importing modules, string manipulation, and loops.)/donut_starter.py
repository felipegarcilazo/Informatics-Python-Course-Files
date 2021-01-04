summ = 0
while True:
    num_input = input('Please enter a number or stop: ')
    if num_input.title() == "Stop":
        break
    summ += int(num_input)
print('The total sum is:', summ)




#while True:
#    file_name = input("Please enter a file name or stop: ")
#    if file_name.title() == 'Stop':
#        break
#    text_file = open(file_name, 'r')
#    print(file_name, 'has', len(file_name.readlines()), 'lines of data in it')
#    text_file.close()



#This program has a problem!

#donuts = eval(input("Aaron, Beth, and Cody go out for donuts." + \
#                   "How many donuts do they buy?: "))

#while donuts >= 3:
#    print("Aaron takes a donut.")
#    print("Beth takes a donut.")
#    print("Cody takes a donut.")
#    donuts -= 3
#if donuts == 0:
#    print("They took all the donuts!")
#else:
#    print("There are", donuts, "left!")	#Here we trace!
