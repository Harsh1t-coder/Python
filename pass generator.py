from datetime import datetime
import random
pdlen = int(input("Enter your password length: "))
char="abcdef$$$$$$$$$$$ghijklmnopqrstu@@#vwxyzABCD#EF@@GHIJKLMNOPQRSTUVWXYZ@@123456789123456789123456789123456789"
s = "".join(random.sample(char,pdlen))
now = datetime.today()
d1 = now.strftime("%d/%m/%Y")
print(f"Password created is : '{s}' and created at '{d1}' ")


