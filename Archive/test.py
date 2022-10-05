from collections import defaultdict

import requests
import bs4

import query_list
import city_list
import consts_fxns

# final_query = "https://www.google.co.in/search?q="+query+"&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICI"+key+encoded_city
text = []

di = defaultdict(list)

for query in query_list.queries:
    li = list()
    for city in city_list.cities:
        encoded_city = consts_fxns.convert_b64(city)
        key = consts_fxns.secret_keys[len(city)]
        final_query = "https://www.google.co.in/search?q=" + query + "&gl=in&hl=en&gws_rd=cr&pws=0&uule=w+CAIQICI" + key + encoded_city
        print(final_query)
        res = requests.get(final_query)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        # print(soup.getText('h3'), soup)
        heading_object = soup.find_all('h3')
        pp = [i.getText() for i in heading_object]
        li.append((city, pp))
    di[query] = li

for q in di:
    print(q)
    for i in range(len(di[q])):
        print(di[q][i][0], di[q][i][1])
# for q in di:
#     city = di[q][0]
#     data = di[q][1]
