import plotparameters.boxplot
import plotparameters.bar as bar
import input.query_list as query_list
import input.city_list as city_list
import psycopg2
import constants.consts_fxns as consts_fxns
import input.db_details

conn = psycopg2.connect(dbname=input.db_details.DB_NAME, user=input.db_details.DB_USER, password=input.db_details.DB_PASS, host=input.db_details.DB_HOST)
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


# # bar graph for tags
# cur.execute("SELECT city, AVG(rbo)::float FROM test_subjects INNER JOIN rbo_table ON rbo_table.qcid=test_subjects.qcid WHERE query IN ('best hospitals','best hospital in india','Covid deaths','covid rules') GROUP BY city;")
# rbo = []
# only_cities = []
# for element in cur.fetchall():
#     only_cities.append(element[0])
#     rbo.append(element[1])

# bar.showbar("Medical related queries",only_cities,rbo)


# #box plot
# data = []
# for city in city_list.cities:
#     cur.execute("SELECT rbo::float FROM test_subjects INNER JOIN rbo_table ON rbo_table.qcid=test_subjects.qcid WHERE city = %s;",(city,))
#     rbo = []
#     for element in cur.fetchall():
#         rbo.append(element[0])
#     data.append(rbo)

# boxplot.showbox(data, only_cities)