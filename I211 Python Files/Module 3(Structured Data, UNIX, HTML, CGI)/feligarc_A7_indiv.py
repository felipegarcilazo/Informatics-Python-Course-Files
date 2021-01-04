import xml.etree.ElementTree as ET

# Question 1
def display_book(parameter):
    root = ET.parse("library.xml")
    elements = root.iter()
    for elem in elements:
        if {'id': parameter} == elem.attrib:
            print("Title:", elem.find('title').text)
            print("Author:", elem.find('author').text)
            print("Cost:", elem.find('price').text)

# Question 2
root = ET.parse("library.xml")
books = root.findall("book")
dates = root.findall("book/publish_date")
genres = root.findall("book/genre")
print("The following books are published in December and Computer books:")
for i in range(len(dates)):
    if "12" == dates[i].text.split("-")[1] and genres[i].text == "Computer":
        display_book(books[i].attrib["id"])

# Question 3
g_list = []
for genre in genres:
    if genre.text not in g_list:
        g_list.append(genre.text)
print("\nAll the genres in the file are:", g_list)
