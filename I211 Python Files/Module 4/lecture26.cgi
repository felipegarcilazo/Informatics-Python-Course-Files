#! /usr/bin/env python3

#print('Content-type: text/html\n')

import MySQLdb

string = "i211f19_feligarc"
password = "my+sql=i211f19_feligarc"

db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)

cursor = db_con.cursor()

def table_create(name):
	funct = "create table"+ name + " (StudentID int(11) NOT NULL AUTO INCREMENT UNIQUE), (Name VARCHAR(25) NOT NULL), (Major VARCHAR(100) NOT NULL), (Email VARCHAR(30)), (Credits INT(11));"
	return funct

def table_insert(name, major, email, credits):
	funct = "INSERT INTO Student(Name, Major, Email, Credits) VALUES(" + name + ", " + major, ", " + email + ", " + credits +")"
	return funct
	
table_create("Student")
table_insert("Felipe", "Informatics", "f@gmail.com", "70")
table_insert("bob", "Computer Science", "bob@gmail.com", "100")
table_insert("John", "Criminal Justice", "john@gmail.com", "80")