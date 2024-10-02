

import sys
import time

print("\nprinting left Diamond using loop: ")
r = 7
c = 4
for i in range(r-2):
    time.sleep(0.5)
    for j in range(c):
        if j < i-1:
            sys.stdout.write("* ")
    print()

for i in range(r):
    time.sleep(0.5)
    for j in range(c):
        if j > i-1:
            sys.stdout.write("* ")
    print()
