from random import choice, randint
from string import ascii_letters, digits

char = ascii_letters + digits

length = int(input("How many characters do you want in your password? (minimum 6, maximum 254) "))
specialChar = input("Need a special character? [y or n] ")

password = "".join(choice(char) for _ in range (length))

if (specialChar == "y"):
	print("\n"+password.replace(password[randint(0, len(password)-1)], "!"))
else:
	print("\n"+password)
