import math
import os
import cap_my_module
import requests

print(math.sqrt(16))
os.abort

print(cap_my_module.sum(3, 8))

r = requests.get("https://www.google.com")
print(r.status_code)