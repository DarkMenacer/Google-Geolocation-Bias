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