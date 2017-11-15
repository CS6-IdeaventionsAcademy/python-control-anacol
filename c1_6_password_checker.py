# Name Alexander Nacol
# Date 11/15/2017
# Python Beginnings
# 6 Password Checker
import time

if "Alexander Nacol" == input("Enter your name: "):
    print("Name correct.")
    if "Bernepugs" == input("What is the password? "):
        print("Access granted. You win.")
    else:
        print("Access denied. System will self destruct in")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("KABOOM")
else:
    print("Access denied. System will self destruct in")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("KABOOM")
        
