#! /usr/bin/env python

import psycopg2

# Pass each psql query as string
# 1. What are the most popular three articles of all time?
articlesQuery = ''' select articles.title as Article,count(*) as hits
             from articles,log
             where log.path=CONCAT('/article/',articles.slug) group by articles.title order by
             hits DESC limit 3; '''


# 2. Who are the most popular authors of all time?
authorsQuery = ''' select authors.name as Author, count(*) as Views
             from log,articles,authors
             where log.path=CONCAT('/article/',articles.slug)
             AND articles.author = authors.id
             Group By authors.name
             order by views DESC '''

# 3. On which days did more than 1% of requests lead to errors?
errorQuery = ''' SELECT date, (fail * 1.0 / total) * 100 FailurePercentage
                FROM (SELECT cast(time as date) date,
                count(*) as total, SUM(CASE status when '404 NOT FOUND'
                then 1 else 0 END) as fail
                FROM log group by date) as notfail
                where ((fail * 1.0 / total) * 1.0) * 100 > 1 '''

#establish connection to makeshift psql instance
def get_query(query):
    '''Makes a get request to news db '''
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close


#create functions which print individual queries
#Query 1
def print_query1(query):
    results = get_query(query)
    print('\nQ1. The 3 most popular articles:\n')
    for i in results:
        print ('\t' + str(i[0]) + ' - ' + str(i[1]) + ' hits')

#Query2
def print_query2(query):
    results = get_query(query)
    print('\nQ2.Most Popular Authors:\n')
    for j in results:
        print ('\t' + str(j[0]) + ' - ' + str(j[1]) + ' views')

#Query3
def print_query3(query):
    results = get_query(query)
    print('\nQ3. Days with more than 1% of requests that lead to an error:\n')
    for k in results:
        print ('\t' + str(k[0]) + ' - ' + str(k[1]) + ' %')

# print out results
print_query1(articlesQuery)
print_query2(authorsQuery)
print_query3(errorQuery)
print("Wow, this required too much effort (with VM which continuously crashed) given the simplicity of what this lesson was trying to convey")
