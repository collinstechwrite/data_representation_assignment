from flask import Flask
from flask_mysqldb import MySQL

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
    headline_title = "banana"
    url = "any_url"
    cur = mysql.connection.cursor()
    #cur.execute('''CREATE TABLE headlinetitles(ID int NOT NULL AUTO_INCREMENT, Title varchar(255), Url varchar(255),PRIMARY KEY (ID));''')
    sqldata = ('''INSERT INTO headlinetitles (Title, Url) VALUES ('%s','%s');''',str(headline),str(url))
    cur.execute(sqldata)
    mysql.connection.commit()
    return 'done!'
