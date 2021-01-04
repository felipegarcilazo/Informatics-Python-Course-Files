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
<!DOCTYPE html>
<html>
<head>
<title>Faculty Delete</title>
<link rel="stylesheet" href="http://cgi.soic.indiana.edu/~dpierz/i211.css">
</head>
<body>
<h1>Faculty Member Deleted!</h1>
<p><a href="FacultyView.cgi">Go Back</a></p>
</body>
</html>
"""

fid = form.getfirst("fid", "Invalid")

sql1 = "Delete FROM Faculty WHERE FacultyID=" + str(fid) + ";"
cursor.execute(sql1)
db_con.commit()

print(html)
