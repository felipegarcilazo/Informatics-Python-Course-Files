#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb

string="i211f19_feligarc"
password="my+sql=i211f19_feligarc"
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, \
passwd=password, db=string)
cursor = db_con.cursor()

html = """
<!DOCTYPE html>
<html>
<head>
	<meta charset='utf-8'>
</head>
<body>
    <h1>Welcome to the Tune Shop</h1>
    <table border='1'>
    <tbody>
    <tr><th>SongID</th><th>Song</th><th>Artist</th><th>Price</th><th>Buy</th></tr>
    {content}
    </tbody>
    </table>        
</body>
</html>
"""

sql = "select * from Songs;"
cursor.execute(sql)
results=cursor.fetchall()

table = ""
for result in results:
    table += "<tr>"
    counter = result[0]
    for item in result:
        table+= "<td>" + str(item) + "</td>"
    table += "<td><a href='Purchased.cgi?song=" + str(counter) + "'>Buy</a></td></tr>"
print(html.format(content = table))