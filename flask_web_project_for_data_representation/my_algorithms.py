import webbrowser
import os
import json
import requests
from newsapi import NewsApiClient
from openpyxl import Workbook, load_workbook
import collections
import matplotlib.pyplot as plt
from flask import Flask, request, render_template



from flask_mysqldb import MySQL

#Port number: 3306

app = Flask(__name__)
app.config['MYSQL_USER'] = 'sql2383132'
app.config['MYSQL_PASSWORD'] = 'qL1!bV7*'
app.config['MYSQL_HOST'] = 'sql2.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql2383132'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

def view_database_records():

    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM headline_titles''')
    mysql.connection.commit()
    


    # print all the first cell of all the rows
    all_the_data = cur.fetchall()

    return all_the_data
    mysql.connection.close()

def receive_text_from_form(text):

    
    #Setting up extractions from News API

    news_keyword = text

    # https://newsapi.org/docs/client-libraries/python
    newsapi = NewsApiClient(api_key='0fb13acc3bc8480eafedb87afa941f7e')


    # /v2/everything
    data = newsapi.get_everything(q=news_keyword)

    jdict = data.get('articles')


    
    my_list = []
    for row in jdict:
        transfer = row['title'],row['url']
        my_list.append(transfer)
    return my_list

    




