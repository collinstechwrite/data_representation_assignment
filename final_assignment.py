#pip install newsapi-python
#pip install xlsx2html
#pip install requests
#pip install googletrans
#pip install pypyodbc
#pip install pymysql

# download mysql connector?
# https://dev.mysql.com/downloads/file/?id=498596

url = "http"
translate_this = "a headline"
translation = "french headline"

a = ("INSERT INTO headline_titles (Title, Language, Translation, Url) VALUES ('"+ translate_this +"','BANNANA', '"+ translation +"', '"+ url +"');")
print(a)










import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pyodbc
import webbrowser
import os




from xlsx2html import xlsx2html



import json
import requests
from newsapi import NewsApiClient








#https://stackoverflow.com/questions/39995802/create-new-access-database-and-tables-using-python

# Database is called news
# CREATE DATABASE news;
# CREATE TABLE headline_titles (ID int NOT NULL AUTO_INCREMENT, Title varchar(255), Language varchar(255), Translation varchar(255), Url varchar(255),PRIMARY KEY (ID));
# INSERT INTO headline_titles (Title, Language, Translation, Url) VALUES ('Dummy Title 3','Spanish', 'Dummy Translation3', 'Dummy Url3');



db = MySQLdb.connect(host="localhost",    # your host, usually localhost
user="root",         # your username
passwd="root",  # your password
db="news")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like


cur.execute("INSERT INTO headline_titles (Title, Language, Translation, Url) VALUES ('Dummy Title 2','BANNANA', 'Dummy Translation 2', 'Dummy Url 2');")

db.commit()
db.close()







news_keyword = input("Input a keyword to search the news:")

LANGUAGES = {
    '1':['Danish','da'], 
    '2':['Dutch','nl'], 
    '3':['Finnish','fi'],
    '4':['French','fr'],
    '5':['German','de'], 
    '6':['Italian','it'], 
    '7':['Japanese','ja'], 
    '8':['Luxembourgish','lb'], 
    '9':['Malay','ms'],
    '10':['Romanian','ro'], 
    '11':['Swedish','sv'], 
    '12':['Tamil','ta']}


for key, value in LANGUAGES.items():
    print (key,value[0])

choose_a_language = input("Choose a number to translate to language: e.g 1 danish")

language_value = LANGUAGES[choose_a_language][1]
language_value2 = LANGUAGES[choose_a_language][0]

print(language_value)

from googletrans import Translator
translator = Translator()





# Init
newsapi = NewsApiClient(api_key='0fb13acc3bc8480eafedb87afa941f7e')



# /v2/everything
all_articles = newsapi.get_everything(q=news_keyword)


print(type(all_articles))
for key in all_articles:
    print(key)

abc = all_articles['articles']

print(abc)


#https://www.programiz.com/python-programming/nested-dictionary
dictionary_length = len(abc)
print(dictionary_length)



row = 0
excel_start_row = 1
column = 0
translated_column = 1
url_column = 2


url=""
translate_this = ""


import xlsxwriter 
workbook = xlsxwriter.Workbook('Example2.xlsx') 
worksheet = workbook.add_worksheet()
worksheet.write(0, column, "English") #writing English to excel
worksheet.write(0, translated_column, language_value2) #writing English to excel 
worksheet.write(0, url_column, "URL")





#https://stackoverflow.com/questions/39995802/create-new-access-database-and-tables-using-python

# Database is called news
# CREATE DATABASE news;
# CREATE TABLE headline_titles (ID int NOT NULL AUTO_INCREMENT, Title varchar(255), Language varchar(255), Translation varchar(255), Url varchar(255),PRIMARY KEY (ID));
# INSERT INTO headline_titles (Title, Language, Translation, Url) VALUES ('Dummy Title 3','Spanish', 'Dummy Translation3', 'Dummy Url3');


"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
user="root",         # your username
passwd="root",  # your password
db="news")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like


cur.execute("INSERT INTO headline_titles (Title, Language, Translation, Url) VALUES ('Dummy Title 2','BANNANA', 'Dummy Translation 2', 'Dummy Url 2');")

db.commit()
db.close()


"""----------------------------------------------------------------------------------------------------------------------------------------------------------"""



# Use all the SQL you like


db = MySQLdb.connect(host="localhost",    # your host, usually localhost
user="root",         # your username
passwd="root",  # your password
db="news")        # name of the data base

        # you must create a Cursor object. It will let
        #  you execute all the queries you need
cur = db.cursor()



while row < dictionary_length:
    #https://docs.python.org/3/tutorial/errors.html
    try:



        
        print(abc[row]['title'])
        translate_this = abc[row]['title']
        translate_this = str(translate_this)
        translation = translator.translate(translate_this, dest=language_value)
        print(translation.text)
        title = translation.text 
        print(abc[row]['url'])
        
        url = abc[row]['url']
        
        worksheet.write(excel_start_row, column, str(translate_this)) 
        worksheet.write(excel_start_row, translated_column, str(title)) 
        worksheet.write(excel_start_row, url_column, str(url))

        
        #check database assignment for handling variables
        a = ("INSERT INTO headline_titles (Title, Language, Translation, Url) VALUES ('"+ translate_this +"','BANNANA', '"+ translation +"', '"+ url +"');")
        cur.execute("INSERT INTO headline_titles (Title, Language, Translation, Url) VALUES ('"+ translate_this +"','BANNANA', '"+ translation +"', '"+ url +"');")
        print(a)

        db.commit()
        

        
        row += 1
        excel_start_row += 1


    except UnicodeEncodeError:
        print('UnicodeEncodeError encountered')
        pass
    except:
        pass

db.close()

#https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/
#json_object = json.dumps(abc, indent = 4)   
#print(json_object)  

#https://www.geeksforgeeks.org/python-create-and-write-on-excel-file-using-xlsxwriter-module/
 
 
  

workbook.close()

#out_stream = xlsx2html('Example2.xlsx')
#out_stream.seek(0)
#print(out_stream.read())


path = os.getcwd()

print("Find yous files here")
print(path+ "/Example2.xlsx")
print(path+ "/Output.html")
# /Users/mbp/Documents/my-project/python-snippets/notebook


print(path)


print(type(path))

#https://pypi.org/project/xlsx2html/
xlsx2html('example2.xlsx', 'Output.html')
webbrowser.open(path + "/Output.html")
