import random,sys
import pyperclip
from llib import *

while True:
	cClear()
	alp = "qwertyuiopasdfghjklzxcvbnm"
	passLenght = int(input("Enter password lenght: "))
	password = ""

	for i in range(passLenght):
		k = random.randint(0,len(alp)-1)
		if random.randint(0,1)==1:
			if random.randint(0,1) == 1:
				password+=alp[k:k+1].upper()
			else:
				password+=alp[k:k+1]
		else:
			password+=str(random.randint(0,9))

	choice = input("| Password generated:\n| - "+password+"\n| 1.Copy to clipboard\n| 2.Save to file\n| >>> ")
	if choice == "1":
		pyperclip.copy(password)
	elif choice == "2":
		saveToFile(password,"passwords.txt","a")
	else:
		print("NO WAY")

