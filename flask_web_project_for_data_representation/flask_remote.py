from flask import Flask
from flask_mysqldb import MySQL
import webbrowser
import os
import json
import requests
from newsapi import NewsApiClient
from openpyxl import Workbook, load_workbook
import collections
import matplotlib.pyplot as plt

#Port number: 3306

app = Flask(__name__)
app.config['MYSQL_USER'] = 'sql2383132'
app.config['MYSQL_PASSWORD'] = 'qL1!bV7*'
app.config['MYSQL_HOST'] = 'sql2.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql2383132'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)



@app.route('/')
def index():

    #Setting up extractions from News API

    news_keyword = 'COVID'

    # https://newsapi.org/docs/client-libraries/python
    newsapi = NewsApiClient(api_key='0fb13acc3bc8480eafedb87afa941f7e')


    # /v2/everything
    data = newsapi.get_everything(q=news_keyword)

    jdict = data.get('articles')

    #WORKING
    for row in jdict:
        cur = mysql.connection.cursor()
        headline = row['title']
        headline = headline.replace("'", "") #remove/replace inverted commas to avoid SQL errors when passing data to database
        url = row['url']
        SQL = ("INSERT INTO headlinetitles (Title, Url) values ('"+ headline +"','"+ url +"');")
        cur.execute(SQL)
        mysql.connection.commit()
    return 'done!'

    #WORKING CODE
    #cur = mysql.connection.cursor()
    #cur.execute('''CREATE TABLE example (id INTEGER, name VARCHAR(20))''')
    #cur.execute('''INSERT INTO example VALUES (1, 'Anthony')''')
    #cur.execute('''INSERT INTO example VALUES (1, 'Anthony')''')
    #mysql.connection.commit()
    #return 'done!'
