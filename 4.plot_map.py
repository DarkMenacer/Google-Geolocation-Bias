import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import psycopg2
import csv
import constants.consts_fxns as consts_fxns
import input.db_details
sns.set_style('whitegrid')

conn = psycopg2.connect(dbname=input.db_details.DB_NAME, user=input.db_details.DB_USER, password=input.db_details.DB_PASS, host=input.db_details.DB_HOST)
cur = conn.cursor()

fp = r'maps/india-polygon.shp'
map_df = gpd.read_file(fp)
map_df_copy = gpd.read_file(fp)


try:
    cur.execute("SELECT rbo_table.qcid,query,city,rbo FROM test_subjects INNER JOIN rbo_table ON rbo_table.qcid=test_subjects.qcid;")
    # cur.execute("SELECT city,AVG(rbo) FROM test_subjects INNER JOIN rbo_table ON rbo_table.qcid=test_subjects.qcid WHERE query IN ('domestic help','Engineering College','Legal Drinking Age','Buy Samosas') GROUP BY city;")
    result = cur.fetchall()
except:
    print(end='')
finally:
    cur.close()
    conn.close()

f = open('temp.csv', 'w', newline='')
spamwriter = csv.writer(f)
spamwriter.writerow(['qcid', 'query', 'city','rbo'])
# spamwriter.writerow(['city', 'rbo'])
spamwriter.writerows(result)
f.close()


df = pd.read_csv("temp.csv")
pd.set_option('display.max_columns', None)
for city in df['city']:
    tmp = city.split(',')
    df['city'] = df['city'].replace(city, tmp[len(tmp)-2])
merged = map_df.set_index('st_nm').join(df.set_index('city'))
merged['rbo'] = merged['rbo'].replace(np.nan, 1)

fig, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('RBO with base city as Delhi for queries', fontdict={'fontsize': '15', 'fontweight' : '8'})

merged.plot(column='rbo',cmap='YlOrRd_r', linewidth=0.8, ax=ax, edgecolor='0',legend=True, markersize=[39.739192, -104.990337],legend_kwds={"label": "rbo"}, vmin=0)
plt.show()
