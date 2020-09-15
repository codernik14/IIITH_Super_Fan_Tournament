import MySQLdb
import subprocess as sp
import pymysql
import mysql.connector
teams = ["OVERALL","CSK","DC","KKR","KXIP","MI","RCB","RR","SRH"]

ipldb = mysql.connector.connect(
  host="localhost",
  username="root",
  password="Chitresh20#"
)
ipl2020 = ipldb.cursor()
ipl = "create database ipl_iiith"
ipl2020.execute(ipl)

ipldb = mysql.connector.connect(
  host="localhost",
  username="root",
  password="Chitresh20#",
  database="ipl_iiith"
)
ipl2020 = ipldb.cursor()

command = "Create Table Players (Roll_no int(10), name VARCHAR(30), username VARCHAR(30), Points decimal(7,2))" 
ipl2020.execute(command)

for i in range(9):
	team_name = teams[i]
	command = "Create Table "
	info = " ( username VARCHAR(30), Points decimal(7,2))"
	team_table = command + team_name + info
	ipl2020.execute(team_table)