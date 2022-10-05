import rbo
import query_list
import city_list
import consts_fxns
import psycopg2

conn = psycopg2.connect(dbname=consts_fxns.DB_NAME, user=consts_fxns.DB_USER, password=consts_fxns.DB_PASS, host=consts_fxns.DB_HOST)
cur = conn.cursor()
data = {}

try:
    for query in query_list.queries:
        data[query] = {}
        for city in city_list.cities:
            cur.execute("SELECT qcid FROM test_subjects WHERE query = %s AND city = %s",(query,city))
            qcid = cur.fetchone()
            cur.execute("SELECT links FROM links_table WHERE qcid = %s",(qcid))
            links = cur.fetchone()
            data[query][city] = links 
            
finally:
    print("RBO Values:\n")
    for query in query_list.queries:
        for city in city_list.cities:
            print(query + " " + city+":",end=' ')
            print(rbo.RankingSimilarity(data[query]["Pune,Maharashtra,India"][0], data[query][city][0]).rbo())
    print(rbo.RankingSimilarity(data["Pen"]["Pune,Maharashtra,India"][0], data["Pen"]["Chennai,Tamil Nadu,India"][0]).rbo())
    print("\n-----")
    cur.close()
    conn.close()
