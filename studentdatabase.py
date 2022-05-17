import mysql.connector

my_database=mysql.connector.connect(host="localhost",
                                   port="8258",
                                   user="root",
                                   passwd="Realoneone1#",)


#Create a cursor to perform tasks
my_cursor= my_database.cursor()

#create a database called studentdatabase

my_cursor.execute("CREATE DATABASE studentdatabase")

#To show the database created

my_cursor.execute("SHOW DATABASES")

for things in my_cursor:
    print(things)

