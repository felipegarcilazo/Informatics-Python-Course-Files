#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb

string = "i211f19_feligarc"
password = "my+sql=i211f19_feligarc"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()

sql = "select * FROM Faculty"
cursor.execute(sql)
results = cursor.fetchall()
print("<h1>Data in the Tables</h1>\n<table border='1'><tbody>")
print("<tr><th>FacultyID</th><th>Name</th><th>Title</th><th>Email</th><th>Areas</th></tr>")
for result in results:
    print("<tr>")
    for data in result:
        print("<td>" + data + "</td>")
    print("</tr>")
print("</tbody></table>")
