import random

#Variables 

length = 15
lowerCase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upperCase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
specials = ["!"," ",'"',"'","#","$","%","&","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","]","\\","]","^","_","`","{","}","|","~"]

available = lowerCase + upperCase + numbers + specials 

password = []

for i in range(length-4):
    password.append(random.choice(available))

password.append(random.choice(lowerCase))
password.append(random.choice(upperCase))
password.append(random.choice(numbers))
password.append(random.choice(specials))
random.shuffle(password)
print(''.join(password))



