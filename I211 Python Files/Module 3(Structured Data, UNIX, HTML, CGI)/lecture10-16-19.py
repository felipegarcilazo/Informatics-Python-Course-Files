import xml.etree.ElementTree as ET
##root = ET.parse("students.xml")
##elements = root.iter()
##first_names = root.findall("Student/name/first")
##last_names = root.findall("Student/name/last")
##print("The students are:")
##for i in range(len(first_names)):
##    print(first_names[i].text, last_names[i].text)

root = ET.parse("students.xml")
elements = root.iter()
fees = root.findall("Student/fees")
fee_total = 0
for fee in fees:
    fee_total += int(fee.text)
print(fee_total)
