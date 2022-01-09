import time
from datetime import datetime
import random

chars = '~!@#$%^&*()_+=-[]\;./<>?{,}|'

print("Current Time: ", datetime.now().strftime('%H:%M:%S %d-%m-%Y'))

ns = input("Please Enter the Size:")
ns = int(ns)
print("Size: ", ns)
nstemp = ns
bksp = '|'

nsym = '*'

i=0
j=0
k=0

ts = 1

unsc = "_"
print(unsc*nstemp*2)

for i in range(ns):
    
    for j in range(ns-1):
        print(bksp*(ns-1), nsym*(ts), bksp*(ns-1))
        ns = ns-1
        ts = ts+2

print(unsc*nstemp*2)

i=0
j=0
ts = 1
ns = nstemp

time.sleep(5)


