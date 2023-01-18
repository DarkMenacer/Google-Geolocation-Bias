import boxplot
import bar
import query_list
import city_list
import psycopg2
import consts_fxns

conn = psycopg2.connect(dbname=consts_fxns.DB_NAME, user=consts_fxns.DB_USER, password=consts_fxns.DB_PASS, host=consts_fxns.DB_HOST)
cur = conn.cursor()


only_cities = []
for city in city_list.cities:
    only_cities.append(city.split(',')[0])


#bar graph
for query in query_list.queries:
    
    cur.execute("SELECT rbo::float FROM test_subjects INNER JOIN rbo_table ON rbo_table.qcid=test_subjects.qcid WHERE query = %s;",(query,))
    rbo = []
    for element in cur.fetchall():
        rbo.append(element[0])

    bar.showbar(query,only_cities,rbo)


#box plot
data = []
for city in city_list.cities:
    cur.execute("SELECT rbo::float FROM test_subjects INNER JOIN rbo_table ON rbo_table.qcid=test_subjects.qcid WHERE city = %s;",(city,))
    rbo = []
    for element in cur.fetchall():
        rbo.append(element[0])
    data.append(rbo)

boxplot.showbox(data, only_cities)