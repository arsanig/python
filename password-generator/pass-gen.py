import random
import string

length = int(input("How many characters do you want in your password? (minimum 6, maximum 254)\n"))

char = string.ascii_letters + string.digits
password = ''.join(random.choice(char) for _ in range (length))

print("\n"+password)