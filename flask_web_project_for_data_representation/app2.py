
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


app = Flask(__name__)
app.config['MYSQL_USER'] = 'sql2383132'
app.config['MYSQL_PASSWORD'] = 'qL1!bV7*'
app.config['MYSQL_HOST'] = 'sql2.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql2383132'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)







@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():



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
            cur = mysql.connection.cursor()
            transfer = row['title'],row['url']
            headline = row['title']
            headline = headline.replace("'", "") #remove/replace inverted commas to avoid SQL errors when passing data to database
            url = row['url']
            my_list.append(transfer)
            SQL = ("INSERT INTO headlinetitles (Title, Url) values ('"+ headline +"','"+ url +"');")
            cur.execute(SQL)
            mysql.connection.commit()
        return my_list


    
    text = request.form['text']







    #get current working directory
    path = os.getcwd()

    
    list = receive_text_from_form(text)
    filelocation = "Find yous files here", path, "/analysis.xlsx"
    
    return render_template("my-form.html", list=list, filelocation=filelocation)




@app.route('/database')
def database():

   #Port number: 3306

    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM headlinetitles''')
    results = cur.fetchall()
    results = str(results)
    return """ 
    <style>
    table.blueTable {
  border: 1px solid #1C6EA4;
  background-color: #EEEEEE;
  width: 100%;
  text-align: left;
  border-collapse: collapse;
}
table.blueTable td, table.blueTable th {
  border: 1px solid #AAAAAA;
  padding: 3px 2px;
}
table.blueTable tbody td {
  font-size: 13px;
}
table.blueTable tr:nth-child(even) {
  background: #D0E4F5;
}
table.blueTable thead {
  background: #1C6EA4;
  background: -moz-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: -webkit-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: linear-gradient(to bottom, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  border-bottom: 2px solid #444444;
}
table.blueTable thead th {
  font-size: 15px;
  font-weight: bold;
  color: #FFFFFF;
  border-left: 2px solid #D0E4F5;
}
table.blueTable thead th:first-child {
  border-left: none;
}

table.blueTable tfoot {
  font-size: 14px;
  font-weight: bold;
  color: #FFFFFF;
  background: #D0E4F5;
  background: -moz-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: -webkit-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: linear-gradient(to bottom, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  border-top: 2px solid #444444;
}
table.blueTable tfoot td {
  font-size: 14px;
}
table.blueTable tfoot .links {
  text-align: right;
}
table.blueTable tfoot .links a{
  display: inline-block;
  background: #1C6EA4;
  color: #FFFFFF;
  padding: 2px 8px;
  border-radius: 5px;
}
</style>   
    
    <table class="blueTable"><thead><tr><th><centre>Database Contents On MySQL Server</centre></th></tr></thead><tbody><tr><td>""" + results + """ </td></tr></tbody></tr></table>
    <img src="static/images/plot.png" alt="A Matplotlibplot">
    <button onclick="goBack()">Go Back</button>

<script>
function goBack() {
  window.history.back();
}
</script>
    """ 






if __name__ == "__main__":
    app.run()
