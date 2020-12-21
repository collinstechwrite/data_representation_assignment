from newsapi import NewsApiClient

#Setting up extractions from News API

news_keyword = 'bitcoin'
# https://newsapi.org/docs/client-libraries/python
newsapi = NewsApiClient(api_key='0fb13acc3bc8480eafedb87afa941f7e')


# /v2/everything
data = newsapi.get_everything(q=news_keyword)

jdict = data.get('articles')


for row in jdict:
    headline = row['title']
    headline = headline.replace("'", "") #remove/replace inverted commas to avoid SQL errors when passing data to database
    url = row['url']
    SQL = ("INSERT INTO headline_titles (Title, Url) VALUES ('"+ headline +"','"+ url +"');")

    sqltest = ('''INSERT INTO headlinetitles (Title, Url) VALUES ('test headline','test url');''')
    print(SQL)
    #INSERT INTO headline_titles (Title, Url) VALUES ('Is the New Visa Bitcoin Rewards Card Worth It?','https://twocents.lifehacker.com/is-the-new-visa-bitcoin-rewards-card-worth-it-1845803159');

    
    print(sqltest)




    
"""
INSERT INTO headline_titles (Title, Url) VALUES ('Is the New Visa Bitcoin Rewards Card Worth It?','https://twocents.lifehacker.com/is-the-new-visa-bitcoin-rewards-card-worth-it-1845803159');
("INSERT INTO headlinetitles (Title, Url) VALUES ('%s','%s');", 'Is the New Visa Bitcoin Rewards Card Worth It?', 'https://twocents.lifehacker.com/is-the-new-visa-bitcoin-rewards-card-worth-it-1845803159')
INSERT INTO headlinetitles (Title, Url) VALUES ('test headline','test url');
INSERT INTO headline_titles (Title, Url) VALUES ('Bitcoin passes $20k and reaches all-time high','http://techcrunch.com/2020/12/16/bitcoin-passes-20k-and-reaches-all-time-high/');
("INSERT INTO headlinetitles (Title, Url) VALUES ('%s','%s');", 'Bitcoin passes $20k and reaches all-time high', 'http://techcrunch.com/2020/12/16/bitcoin-passes-20k-and-reaches-all-time-high/')
"""
