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
<head>
<title>Faculty Add</title>
<link rel="stylesheet" href="http://cgi.soic.indiana.edu/~dpierz/i211.css">
</head>
<body>
<h1>New Faculty Member Added!</h1>
<table border="1" width="100%">
<tbody>
<tr>
<th>Faculty ID</th>
<th>Name</th>
<th>Title</th><th>Email</th><th>Areas</th>
</tr>
{content}
</tbody>
</table>
</body>
</html>"""

name = form.getfirst("name", "Invalid Name")
title = form.getfirst("title", "Invalid Title")
email = form.getfirst("email", "Invalid Email")
area = form.getfirst("areas", "Invalid Area")

sql1 = "INSERT INTO Faculty(Name, Title, Email, Areas) VALUES ('" + name + \
       "', '" + title + "', '" + email + "', '" + area + "');"
cursor.execute(sql1)
db_con.commit()

sql2 = "select * from Faculty;"
cursor.execute(sql2)
results=cursor.fetchall()

table = ""
for result in results:
    table += "<tr>"
    for item in result:
        table+= "<td>" + str(item) + "</td>"
    table += "</tr>"

print(html.format(content = table))


