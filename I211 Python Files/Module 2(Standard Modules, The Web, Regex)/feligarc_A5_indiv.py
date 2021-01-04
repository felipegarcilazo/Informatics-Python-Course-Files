#Felipe Garcilazo
#Group 15

## Question 1
### The %B

##Question 2
### Import the csv and date module module
### First open the ShopRecords.csv file.
### Create a list that will store all the items sold.
### Create a loop
### and inside of the loop, and if the date lands on a weekend print out the items sold with the associated text

##Question 3
import csv, datetime
csv_file = csv.DictReader(open("ShopRecords.csv", "r"))
for entry in csv_file:
    split_date = entry["Date"].split("/")
    if datetime.date(int(split_date[2]), int(split_date[0]), int(split_date[1])).strftime("%A") \
       in ("Saturday", "Sunday"):
        print(entry["Item"])
