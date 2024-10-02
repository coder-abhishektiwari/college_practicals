#Practical 4: Write a python script to print the current date in the following format “Sun May 29 02:26:23 IST 2017”

#importing time library
import time

print()
#fetching and formating time
print("Date and time fetched from os")
current_time = time.strftime("%a %b %d %H:%M:%S %Z %Y")

#printing date and time
print("current date and time is: ",current_time)   #current date and time is:  Wed Aug 28 23:04:51 India Standard Time 2024
print()