#! /usr/bin/env python
import psycopg2
import pycodestyle

# Pass each psql query as string
# 1. What are the most popular three articles of all time?
articlesQuery = ''' select articles.title as Article,
             count(*) as hits
             from articles,log
             where log.path = CONCAT('/article/',articles.slug)
             group by articles.title order by
             hits DESC limit 3; '''

#Place the articles query within a function whichc will later be called
def print_query1(query):
    results = get_query(query)
    print('\nQ1.The 3 most popular articles:\n')
    for i in results:
        print ('\t' + str(i[0]) + ' - ' + str(i[1]) + ' hits')



# 2. Who are the most popular authors of all time?
authorsQuery = ''' select authors.name as Author, count(*) as Views
             from log,articles,authors
             where log.path=CONCAT('/article/',articles.slug)
             AND articles.author = authors.id
             Group By authors.name
             order by views DESC '''

##Place the articles query within a function whichc will later be called
def print_query2(query):
    results = get_query(query)
    print('\nQ2.Most Popular Authors:\n')
    for j in results:
        print ('\t' + str(j[0]) + ' - ' + str(j[1]) + ' views')


# 3. On which days did more than 1% of requests lead to errors?
errorQuery = ''' select date, (fail * 1.0/ total) * 100 FailurePercentage
                FROM (SELECT cast(time as date) date,
                count(*) as total, SUM(CASE status when '404 NOT FOUND'
                then 1 else 0 END) as fail
                FROM log group by date) as notfail
                where ((fail * 1.0/ total) * 1.0) * 100 > 1 '''

##Place the articles query within a function whichc will later be called
def print_query3(query):
    results = get_query(query)
    print('\nQ3.error days:\n')
    for k in results:
        print ('\t' + str(k[0]) + ' - ' + str(k[1]) + ' %')

#establish connection to makeshift psql instance
def get_query(query):
    '''Connect to news db'''
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    return c.fetchall()


# print out results
print_query1(articlesQuery)
print_query2(authorsQuery)
print_query3(errorQuery)
