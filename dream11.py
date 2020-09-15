from selenium import webdriver
import time
import MySQLdb
import subprocess as sp
import pymysql
import mysql.connector
    
driver = webdriver.Chrome()
driver.get('https://www.dream11.com/login')
mobile_no = '/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/div[1]/div[2]/div[1]/input'
driver.find_element_by_xpath(mobile_no).send_keys(8602579879)

proceed = '/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/div[2]/button'
driver.find_element_by_xpath(proceed).click()

otp='/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/input'
s = (input("OTP: "))
driver.find_element_by_xpath(otp).send_keys(s)

verify = '/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/button'
driver.find_element_by_xpath(verify).click()


match_link = input("Contest_link: ")
driver.get(match_link)

ipldb = mysql.connector.connect(
  host="localhost",
  username="root",
  password="Chitresh20#",
  database="ipl_iiith"
)
ipl2020 = ipldb.cursor()

command = "Create Table temp (username VARCHAR(30), Points decimal(7,2))"
ipl2020.execute(command)

j = 1
while True:
    # print(j)
    j+=1
    time.sleep(5)
    names = driver.find_elements_by_class_name('playerName_1ac16')
    points = driver.find_elements_by_class_name("pointsInfo_a01d9")

    for i in range(len(names)):
        com1 = "Insert Into temp (username , Points) VALUES (%s,%s)"
        com2 = "Insert Into CSK (username , Points) VALUES (%s,%s)"
        com3 = "Insert Into MI (username , Points) VALUES (%s,%s)"
        com4 = "Insert Into OVERALL (username , Points) VALUES (%s,%s)"
        val = (names[i].text , (points[i].text.strip()))
        ipl2020.execute(com1,val),
        v1 = (names[i].text , "20")
        ipl2020.execute(com2,v1)
        ipl2020.execute(com3,v1)
        ipl2020.execute(com4,v1)
    try : 
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[3]/div/div[2]/div[2]/div[3]/div[3]/div[2]/button').click()
    except:
        break

ipldb.commit()

team1 = input("Team 1: ")
team2 = input("Team 2: ")
team3 = "OVERALL"
sql="Select * From temp"

def upd(team):
    ipl2020.execute(sql)
    results = ipl2020.fetchall()
    for row in results:
        uname = "'" + row[0] + "'"
        pts = row[1]
        c1 = "Select * From " + team + " Where username = " + uname 
        ipl2020.execute(c1)
        a = ipl2020.fetchall()
        if len(a)==0:
            continue
        else:
            val=float(a[0][1]) + float(pts)
            c2 = "Update " + team + " Set Points = " + str(val) + " Where username = " + uname
            ipl2020.execute(c2)


upd(team1)
upd(team2)
upd(team3)

ipl2020.execute("Drop Table temp")
ipldb.commit()