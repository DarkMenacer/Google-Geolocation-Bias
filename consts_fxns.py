import base64

def convert_b64 (value):
    value_bytes = value.encode("ascii")
    base64_bytes = base64.b64encode(value_bytes)
    return base64_bytes.decode("ascii")

secret_keys = {}
for i in range(0, 26):
    secret_keys.setdefault(i,chr(i+65))
for i in range(26,52):
    secret_keys.setdefault(i,chr(i+71))

DB_HOST = "Pranavs-MacBook-Pro.local"
DB_NAME = "google_bias"
DB_USER = "pranavchatur"
DB_PASS = "psql"

def display(x):
    for element in x:
        print(element.get_attribute("href"))

def adjust_links(link_elements, peep_also_ask):
    k = 0; flag = False
    for i in range(len(link_elements)):
        for j in range(i,len(link_elements)):
            if str(link_elements[j]) != str(peep_also_ask[k]):
                k = 0
                break
            else:
                k+=1
                if(k == len(peep_also_ask)): 
                    flag = True
                    break
        if flag: break
    if flag == False: 
        print("Sub-array absent! no change in link_elements")
    else:
        counter = 0
        while(counter < j+1-i):
            print(str(link_elements[i].get_attribute("href"))+ " is removed")
            link_elements.remove(link_elements[i])
            counter+=1
    return link_elements
            
""" def print_diff(g1,g2):
    for m in g1:
        if find_in(m,g2) == 0:
            print(m)
    print("This is the difference") """

def doppleganger(g1):
    occ = {}
    for m1 in g1:
        occ[m1] = 0
    for m1 in g1:
        for m2 in g1:
            if m1 == m2:
                occ[m1]+=1
    for m1 in g1:
        if occ[m1] > 1:
            print(m1)
    print("This is the doppleganger\n")
    print("This is the links table but organised:")
    for key, value in occ.items():
        print(key + " = " + str(value))
    print()

def should_store(x, links):
    for link in links:
        if x == link:
            return 0
    return 1