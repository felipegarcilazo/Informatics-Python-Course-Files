import xml.etree.ElementTree as ET

def id_find(num):
    root = ET.parse(source="students.xml")
    ids = root.findall("Student/id")
    f_names = root.findall("Student/name/first")
    l_names = root.findall("Student/name/last")

    for i in range(len(ids)):
        if ids[i].text == num:
            return f_names[i].text + " " + l_names[i].text
    return "Not Found"

def fee_find(name):
    root = ET.parse(source="students.xml")
    fname, lname = name.split(" ")
    f_names = root.findall("Student/name/first")
    l_names = root.findall("Student/name/last")
    fees = root.findall("Student/fees")
    
    for i in range(len(f_names)):
        if f_names[i].text == fname and l_names[i].text == lname:
            return name + " owes " + fees[i].text + " " + \
                   fees[i].attrib['units'] + " " + fees[i].attrib['c'] + \
                   " in fees."
    return "NOt FOund"

print(fee_find("Rose Dawson"))
print(fee_find("Jack Sparrow"))
print(fee_find("No Body"))
