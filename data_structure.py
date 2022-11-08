import rbo
import query_list
import city_list
import consts_fxns
import psycopg2

conn = psycopg2.connect(dbname=consts_fxns.DB_NAME, user=consts_fxns.DB_USER, password=consts_fxns.DB_PASS, host=consts_fxns.DB_HOST)
cur = conn.cursor()
data = {}

try:
    cur.execute("TRUNCATE TABLE rbo_table")
    conn.commit()
    print("The rbo table is erased")

    for query in query_list.queries:
        data[query] = {}
        for city in city_list.cities:
            cur.execute("SELECT qcid FROM test_subjects WHERE query = %s AND city = %s",(query,city))
            qcid = cur.fetchone()
            cur.execute("SELECT links FROM links_table WHERE qcid = %s",(qcid))
            links = cur.fetchone()
            data[query][city] = links 
            
    print("RBO Values:\n")
    for query in query_list.queries:
        for city in city_list.cities:
            print(query + " " + city+":",end=' ')
            if(len(data[query][city][0]) != len(set(data[query][city][0]))):
                print(len(data[query][city][0]), len(set(data[query][city][0])))
                consts_fxns.doppleganger(data[query][city][0])
            else:
                val = rbo.RankingSimilarity(data[query][city_list.base_city][0], data[query][city][0]).rbo()
                cur.execute("SELECT qcid FROM test_subjects WHERE query = %s AND city = %s",(query,city))
                qcid = cur.fetchone()
                cur.execute("INSERT INTO rbo_table (qcid, rbo) VALUES (%s,%s);",(qcid,val))
                conn.commit()
                print(val)
finally:
    print("\n-----")
    cur.close()
    conn.close()
