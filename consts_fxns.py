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

#function was created to test whether same link is being stored twice, apparently it is not
def find_in(x, links):
    exists = 0
    for link in links:
        if x != link:
            exists = 1
            break
    return exists



def print_diff(g1,g2):
    for m in g1:
        if find_in(m,g2) == 0:
            print(m)
    print("This is the difference")



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
    print("This is the doppleganger")
