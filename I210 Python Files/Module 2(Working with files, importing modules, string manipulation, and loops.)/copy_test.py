import os
contents = os.listdir(os.getcwd())
txt_files = []
for files in contents:
    if files[-4:] == '.txt':
        txt_files.append(files)
print(txt_files)




#text_file = open("numbers.txt", 'r')
#file_contents = text_file.readlines()
#text_file.close()
#number = 0
#for line in file_contents:
#    number += int(line)
#print('The total is:', number)





#def copy_file(filename_from, filename_to):
    
    #write code here to open the first file
#    file1 = open(filename_from, 'r')
#    copied_contents = file1.readlines()
#    file1.close()
    #read it, and copy the data
#    file2 = open(filename_to, 'w')
#    file2.write(copied_contents)
#    file2.close()
    #into the second file

#testcode
#file_f = input("Please enter the name of the file to copy FROM: ")
#file_t = input("Please enter the name of the file to copy TO: ")
#copy_file(file_f , file_t)
#print("The content of", file_f, "has been copied into", file_t, ".")





