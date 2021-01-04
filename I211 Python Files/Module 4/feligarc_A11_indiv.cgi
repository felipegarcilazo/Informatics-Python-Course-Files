#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb
string="i211f19_feligarc"
password="my+sql=i211f19_feligarc"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, \
passwd=password, db=string)
cursor = db_con.cursor()

sql = "select Name from item;"
cursor.execute(sql)
results=cursor.fetchall()

radio_buttons = ""
for result in results:
	radio_buttons+="<input type='radio' name='item' value = '" + str(result[0]) + "'>"\
	 +  str(result[0])  + "<br>" 

html = """
<html>
<head>
<meta charset="utf-8">
<title>Robot Delivery System</title>
</head>
<body>
	<form action="delivery_table.cgi" method="post">
		<h1>What would you like to have delivered?</h1>
		{items}
		<h2>Cost($):</h2>
		<input type = "text" name = "cost">
		<h2>Delivery Method</h2>
		<input type="radio" name="method" value="a">Flying Drone ($10)
		<br>
		<input type="radio" name="method" value="b">Self Driving Car ($20)
		<br>
		<input type="radio" name="method" value="c">Giant Robot ($100)
		<br>
		<button type="submit">Submit</button>
	</form>
</body>
</html>"""

print(html.format(items=radio_buttons))