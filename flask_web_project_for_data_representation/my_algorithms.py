#need to create a function receive_text_from_form(str(text))


#Necessary pip installs from work on previous versions (more may be needed if program says module missing on your computer)

#pip install newsapi-python
#pip install xlsx2html
#pip install requests
#pip install pypyodbc
#pip install pymysql
#pip install openfoodfacts==0.1.2

"--------------------------------------------------------------------------------------------------------------------------------------------------------"""

# Database is called news

# DROD DATABASE news;

# CREATE DATABASE news;
# USE news;
# CREATE TABLE headline_titles(ID int NOT NULL AUTO_INCREMENT, Title varchar(255), Url varchar(255),PRIMARY KEY (ID));


"--------------------------------------------------------------------------------------------------------------------------------------------------------"""


#Setting up the imports

import webbrowser
import os
import json
import requests
from newsapi import NewsApiClient
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from openpyxl import Workbook, load_workbook
import collections
import matplotlib.pyplot as plt


def View_Added_Database_Records():
    print("View Added Database Records")
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    user="root",         # your username
    passwd="root",  # your password
    db="news")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM headline_titles")

    # print all the first cell of all the rows
    all_the_data = cur.fetchall()
    print(all_the_data)
    

    db.close()



"--------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Updating spreadsheet

Row_Incrementer = 1

workbook = Workbook()
sheet = workbook.active
sheet["A" + str(Row_Incrementer)] = "Headline Title"
sheet["B" + str(Row_Incrementer)] = "URL"
workbook.save(filename="analysis.xlsx")
workbook.close()


def excel_row_update(headline_title, url):

    global Row_Incrementer
    Row_Incrementer += 1

    workbook = load_workbook(filename="analysis.xlsx")
    sheet = workbook.active

    sheet["A" + str(Row_Incrementer)] = headline_title
    sheet["B" + str(Row_Incrementer)] = url

    workbook.save(filename="analysis.xlsx")
    workbook.close()
    print("success added:",headline_title, url, "to spreadsheet")


def database_row_update(headline_title, url):

    #Connect to MySQL database

    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    user="root",         # your username
    passwd="root",  # your password
    db="news")        # name of the data base

        # you must create a Cursor object. It will let
        #  you execute all the queries you need
    cur = db.cursor()


    #check database assignment for handling variables
    SQL = ("INSERT INTO headline_titles (Title, Url) VALUES ('"+ headline_title +"','"+ url +"');")
    print(SQL)
    cur.execute("INSERT INTO headline_titles (Title, Url) VALUES ('"+ headline_title +"','"+ url +"');")
    db.commit()
    db.close()


"--------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Setting up extractions from News API

news_keyword = input("Write a keyword to search the news , e.g. bitcoin")

# https://newsapi.org/docs/client-libraries/python
newsapi = NewsApiClient(api_key='0fb13acc3bc8480eafedb87afa941f7e')


# /v2/everything
data = newsapi.get_everything(q=news_keyword)


for key in data:
    print(key)

jdict = data.get('articles')

#for row in jdict:
    #print(row['title'])


"--------------------------------------------------------------------------------------------------------------------------------------------------------"""
#Setting up variables before the loop, these handle the number of iterations in the loop and position to publish content to excel

row = 0
excel_start_row = 1


column = 0
url=""


"--------------------------------------------------------------------------------------------------------------------------------------------------------"""


my_string_for_word_count = "" #this string will be used for doing word count analysis

#The while loop below handle printing to console, saving to excel, saving to database



for row in jdict:
    
    #https://docs.python.org/3/tutorial/errors.html
    try:
      

        headline_title = row['title']
        headline_title = headline_title.replace("'", "") #remove/replace inverted commas to avoid SQL errors when passing data to database

        url = row['url']
        print("Title", headline_title)
        print("url:", url)


        my_string_for_word_count = my_string_for_word_count + headline_title #adding one healine at a time to the string for word count analysis
        excel_row_update(headline_title, url) #update spreadsheet
        database_row_update(headline_title, url) #update database
        
                


    except UnicodeEncodeError:
        print('UnicodeEncodeError encountered')
        break
    except:
        break

"--------------------------------------------------------------------------------------------------------------------------------------------------------"""
#get current working directory so that files can be published and saved to same folder as the python app
path = os.getcwd()

print("Find yous files here")
print(path+ "/analysis.xlsx")

"--------------------------------------------------------------------------------------------------------------------------------------------------------"""

print("view all the data in the database table")
View_Added_Database_Records()

"--------------------------------------------------------------------------------------------------------------------------------------------------------"""
#this code below does a word count analysis
#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php
def word_count(str):
    counts = {}
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

counted_words =  word_count(my_string_for_word_count)


sorted_dict = collections.OrderedDict(counted_words)



x = sorted_dict

#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
sorted_x = sorted(x.items(), key=lambda kv: kv[1])


#https://stackoverflow.com/questions/646644/how-to-get-last-items-of-a-list-in-python
my_graph_data = list(sorted_x)[-10:]
my_graph_data_dict = dict(my_graph_data)



#https://thispointer.com/different-ways-to-remove-a-key-from-dictionary-in-python/
common_words = ['the',
'of',
'and',
'a',
'to',
'in',
'is',
'you',
'that',
'it',
'he',
'was',
'for',
'on',
'are',
'as',
'with',
'his',
'they',
'I',
'at',
'be',
'this',
'have',
'from',
'or',
'one',
'had',
'by',
'word',
'but',
'not',
'what',
'all',
'were',
'we',
'when',
'your',
'can',
'said',
'there',
'use',
'an',
'each',
'which',
'she',
'do',
'how',
'their',
'if',
'will',
'up',
'other',
'about',
'out',
'many',
'then',
'them',
'these',
'so',
'some',
'her',
'would',
'make',
'like',
'him',
'into',
'time',
'has',
'look',
'two',
'more',
'write',
'go',
'see',
'number',
'no',
'way',
'could',
'people',
'my',
'than',
'first',
'been',
'call',
'who',
'its',
'now',
'find',
'long',
'down',
'day',
'did',
'get',
'come',
'made',
'may',
'part',
]

for word in common_words:
    try:
        my_graph_data_dict.pop(word)
    except:
        continue

#https://www.kite.com/python/answers/how-to-plot-a-bar-chart-using-a-dictionary-in-matplotlib-in-python
a_dictionary = x
keys = my_graph_data_dict.keys()
values = my_graph_data_dict.values()

#https://www.kite.com/python/answers/how-to-rotate-axis-labels-in-matplotlib-in-python
plt.xticks(rotation=45)
plt.yticks(rotation=90)
#https://showmecode.info/matplotlib/bar/change-bar-color/
plt.bar(keys, values,  color=['red', 'blue', 'purple', 'green', 'lavender'])
plt.ylabel('Occurences of word')
plt.title('Most Frequent Words In Headlines')
#https://www.kite.com/python/answers/how-save-a-matplotlib-plot-as-a-pdf-file-in-python
plt.savefig("plots.pdf")
plt.show()

"--------------------------------------------------------------------------------------------------------------------------------------------------------"""



