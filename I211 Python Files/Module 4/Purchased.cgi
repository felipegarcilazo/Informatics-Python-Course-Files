#! /usr/bin/env python3
print('Content-type: text/html\n')

import MySQLdb, cgi
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
<meta charset='utf-8'>
</head>
<body>
    <h1>Purchased Records</h1>
    <table border='1'>
    <tbody>
    <tr><th>Song</th><th>Purchased Times</th></tr>
    {content}
    </tbody>
    </table>        
</body>
</html>
"""

song = form.getfirst("song", "Invalid")

sql1 = "INSERT INTO Purchased(Song) VALUES (" + str(song) + ");"
cursor.execute(sql1)
db_con.commit()

sql2 = "SELECT s.Song, COUNT(s.Song) FROM Purchased AS p, Songs AS s WHERE p.Song = s.SongID GROUP BY Song;"
cursor.execute(sql2)
results=cursor.fetchall()

table = ""
for result in results:
    table += "<tr>"
    for item in result:
        table+= "<td>" + str(item) + "</td>"
    table += "</tr>"
    
print(html.format(content=table))
