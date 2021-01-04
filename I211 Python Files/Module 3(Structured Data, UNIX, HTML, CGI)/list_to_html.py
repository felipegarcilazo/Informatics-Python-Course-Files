import re
##data = [["Item", "Cost", "Type"], ["Coke", "$2", "Drink"],
##        ["Water", "$0", "Drink"], ["Fries", "$4", "Appetizer"],
##        ["Onion Rings", "$3", "Appetizer"], ["Steak", "$12", "Entree"],
##        ["Chicken", "$8", "Entree"], ["Caesar Salad", "$7", "Entree"]]
##html = """<!doctype html>
##<html>
##<head><meta charset="utf-8">
##    <link rel="stylesheet" href="https://cgi.sice.indiana.edu/~dpierz/i211.css">
##    <title>Google Link</title>
##</head>
##<body>
##    <table border=1>
##        {content}
##    </table>
##</body>
##</html>"""
##
##data_entry = ''
##for lists in data:
##    data_entry += '<tr>'
##    for entry in lists:
##        data_entry += '<td>'+entry+'</td>'
##    data_entry += '</tr>'
##    
##
##out = open("table_website.html", "w")
##out.write(html.format(content=data_entry))
##out.close()
##
##print("done")

file = open("table_website.html", "r")
content = file.read()
file.close()
content_table = re.findall('(?<=<tr>).+?(?=</tr>)', content, re.DOTALL)
data = []
print("Data loaded from file:")
for content in content_table:
    data += [re.findall('(?<=<td>).+?(?=</td>)', content, re.DOTALL)]
print(data)
