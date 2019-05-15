import csv
import pymysql 
import datetime

#Load text file into list with CSV module
with open('ACC.txt', 'rt') as f:
	reader = csv.reader(f, delimiter = ',', skipinitialspace=True)
	lineData = list()
	cols = next(reader)

	for line in reader:
		if line != []:
			lineData.append(line)

#Connect with database
cnx = pymysql.connect(user = 'root', password = 'vibha123',
						  host = '127.0.0.1',
						  database = 'mydb')

cursor = cnx.cursor()
#cursor.execute("CREATE TABLE aac (`name` varchar(36) DEFAULT NULL,`date` date DEFAULT NULL , `time` time, `P1` real, `P2` real,`P3` real,`P4` real,`P5` real)")
cursor.execute("SHOW TABLES")
for tb in cursor:
	print(tb)
#Writing Query to insert data
query = "INSERT INTO aac (name, date, time, P1, P2, P3,P4,P5) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"

#Change every item in the sub list into the correct data type and store it in a directory
for i in range(len(lineData)):
	taxi = (lineData[i][0], (lineData[i][1]), (lineData[i][2]), (lineData[i][3]), (lineData[i][4]), lineData[i][5], (lineData[i][6]), (lineData[i][7]))
	cursor.execute(query, taxi) #Execute the Query

#Commit the query
cnx.commit()
cnx.close()
			