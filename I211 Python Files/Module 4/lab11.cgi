#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb
string="i211f19_feligarc"
password="my+sql=i211f19_feligarc"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, \
passwd=password, db=string)
cursor = db_con.cursor()

sql = "select Name from Robot;"
cursor.execute(sql)
results=cursor.fetchall()

droppdown = ""
for result in results:
        dropdown +="<option>" + str(result[0]) + "</option>"

html = """
<html>
<head><title>Robot Fight!</title><link rel="stylesheet" href="http://cgi.soic.indiana.edu/~dpierz/i211.css">
</head>
<body>
    <H1>Choose two robots to face off!</H1>
    <FORM method="post" action="robot_fight.cgi">
        <H3>Please select robots:</H3>
        <p> Robot Name:
        <select name="robot1">
        {content1}
        </select>
        <select name="robot2">
        {content2}
        </select>
        </p>
        <button type="submit" />Battle!</button>
    </FORM>
    </body>
</html>
"""

print(html.format(content1=dropdown, content2=dropdown))
