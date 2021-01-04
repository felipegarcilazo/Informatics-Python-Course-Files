#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi
form = cgi.FieldStorage()
html = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Robot Delivery System Confirmation</title>
</head>
<body>
    <h1>Robot Delivery System Confirmation</h1>
    <p>You have selected to have {content1} delivered by {content2}</p>
    <p>Your total comes to {content3}</p>
</body>
"""

item = form.getfirst("item", "invalid item")
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
    total_price = int(form.getfirst("cost", 0))+ int(delivery_cost)
except:
    total_price = "Invalid cost entered!!"

print(html.format(content1 = item, content2 = transport, content3 = "$" + str(total_price)))
