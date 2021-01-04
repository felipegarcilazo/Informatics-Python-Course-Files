#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb

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
<th>Delete</th>
</tr>
{content}
</tbody>
</table>
</body>
</html>"""

sql = "select * from Faculty;"
cursor.execute(sql)
results=cursor.fetchall()

table = ""
for result in results:
    table += "<tr>"
    counter = result[0]
    for item in result:
        table+= "<td>" + str(item) + "</td>"
    table += "<td><a href='FacultyDelete.cgi?fid=" + str(counter) + \
             "'>Delete</a></td></tr>"
    counter += 1
print(html.format(content = table))
