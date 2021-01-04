#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi, MySQLdb, random
form=cgi.FieldStorage()

string="i211f19_feligarc"
password="my+sql=i211f19_feligarc"
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, \
passwd=password, db=string)
cursor = db_con.cursor()

html = """
<!doctype html>
<html>
<head><title>Robot Fight!</title><link rel="stylesheet" href="http://cgi.soic.indiana.edu/~dpierz/i211.css">
</head>
<body>
    <p>{robot_win} wins round with its {weapon}. {robot_loss} is now deactivated</p>
</body>
</html>
"""

robotlist = [form.getfirst("robot1", "Megatron"), form.getfirst("robot2", "Megatron")]
robot_win = random.choice(robotlist)
robotlist.remove(robot_win)
robot_lose = robotlist[0]

sql1 = "SELECT Weapon FROM Robot WHERE Name='" + robot_win + "';"
cursor.execute(sql1)
results=cursor.fetchall()
winner_weapon = results[0]

sql2 = "Update Robot SET Active = 'False' Where Name ='" + robot_lose + "';"
cursor.execute(sql2)
db_con.commit()

print(html.format(robot_win = robot_win, robot_loss = robot_lose, weapon = winner_weapon))
