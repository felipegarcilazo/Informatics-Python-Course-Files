#Felipe Garcilazo Group 15

## Question 1
## https://docs.python.org/3.7/library/index.html

## Question 2


## Question 3
### First import os
### Ask the user for an input that is a path to a directory
### Loop through the list of the contents in the specified directory
### If the contents is a file and has draft in it then
### Rename the file with the part that is draft to final
### Else leave the directory alone.

import os, datetime

usr_direct = input("Enter a path to a directory: ")
for content in os.listdir(usr_direct):
    if os.path.isfile(content) and "draft" in content:
        # This is the bonus part
        file_content = [sentence for sentence in open(content, "r")]
        file_content += "\nEdited on:" + str(datetime.date.today())
        with open(content, "w") as writ_to_fle:
            writ_to_fle.writelines(file_content)
        # This is the renaming part of problem 3
        os.rename(content, content.replace("draft", "final"))

