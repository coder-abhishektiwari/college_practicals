import time
ctime = time.strftime("%H:%M:%S")
date = time.strftime("%D")

print("Loading time \nplease wait")
time.sleep(3)


for i in range(101):
    time.sleep(0.05)
    print("Loading",i, "%","."*i)

time.sleep(1)
print("Loaded")

print("Time: ", ctime)
print("Date: ", date)
