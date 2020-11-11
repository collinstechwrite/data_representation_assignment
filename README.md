#Necessary pip installs from work on previous versions (more may be needed if program says module missing on your computer)

## pip install newsapi-python
## pip install xlsx2html
## pip install requests
## pip install googletrans
## pip install pypyodbc
## pip install pymysql
## pip install openfoodfacts==0.1.2


Before running this python application all necessary PIP installs will need to be done.

Before running this python application a MySQL database will need to be installed

The current username and password programmed into this python application for MySQL access is root , root

See settings below

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    user="root",         # your username
    passwd="root",  # your password
    db="news")

The user of this python application will need to setup a MySQL database on their local host.

This can be done with the following MySQL code



CREATE DATABASE news;
USE news;
CREATE TABLE headline_titles(ID int NOT NULL AUTO_INCREMENT, Title varchar(255), Language varchar(255), Translation varchar(255), Url varchar(255),PRIMARY KEY (ID));



This programs extract brand names that sell food from the openfoodfacts api
This program then searches newsapi for newspaper headlines using a brand name chosen by the user
This program then translates the newspaper headlines into a language chosen by the user - API key was required
This program then saves the translated results to a spreadsheet called analysis.xlsx
This program then saves the translated results to a MySQL database called news - It is requirement that user has database news setup on their local host and same passwords as above.
This program will then attempt to convert the spreadsheet results into a webpage called Output.html and load the webbrowser







