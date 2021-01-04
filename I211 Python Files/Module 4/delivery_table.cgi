#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi, MySQLdb
form=cgi.FieldStorage()

string="i211f19_feligarc"
password="my+sql=i211f19_feligarc"
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, \
passwd=password, db=string)
cursor = db_con.cursor()

html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Robot Delivery System Confirmation</title>
<link rel="stylesheet" href="http://cgi.soic.indiana.edu/~dpierz/i211.css">
</head>
    <body>
    <h1>Robot Delivery System Confirmation</h1>
    <p>You have selected to have a {content1} delivered by {content2}.</p>
    <p>Your total comes to {content3}</p>
<h2>Delivery Records</h2>
{content4}
</body>
</html> 
"""

items = form.getfirst("item", "unknown item")

if form.getfirst("method") == "a":
    delivery_cost = 10
    transport = "Flying Drone"
elif form.getfirst("method") == "b":
    delivery_cost = 20
    transport = "Self Driving Car"
elif form.getfirst("method") == "c":
    delivery_cost = 100
    transport = "Giant Robot"
else:
    delivery_cost = 0
    transport = "Unknown Method"
    
try:
    total_price = int(form.getfirst("cost", 0)) + int(delivery_cost)
except:
    total_price = "Invalid cost entered!!"
    
sql1 = "INSERT INTO Deliveries (Item, Cost, Method, Shipping) VALUES('" + items + "', " + \
str(total_price) + ", '" + transport + "', " + str(delivery_cost) + ");"
cursor.execute(sql1)
db_con.commit()

sql2 = "select Item, Cost, Method, Shipping from Deliveries;"
cursor.execute(sql2)
results=cursor.fetchall()
table = "<table border='1'><tbody><tr><th>Item</th><th>Cost</th><th>Method</th><th>" + \
"Shipping</th></tr>"
for result in results:
	table += "<tr>"
	for item in result:
		table += "<td>" + str(item) + "</td>"
	table+= "</tr>"
table+="</tbody></table>"

print(html.format(content1 = items, content2 = transport, content3 = "$" + \
str(total_price), content4 = table))