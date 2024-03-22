import random 

print("Welcome to the Password Generator! ")

number1 = int(input("Enter the required no. of Numbers: "))
letter1 = int(input("Enter the required no. of Letters: ")) 
symbol1 = int(input("Enter the required no. of Symbols: ")) 

number = ['0','1','2','3','4','5','6','7','8','9']
letter = ['a','b','c','d','e','f','g','h','i','j','k','l',
          'm','n','o','p','q','r','s','t','u','v','w','x',
          'y','z','A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T','U','V',
          'W','X','Y','Z'] 
symbol =['!','@','$','#','%','^','&','*','(',')','+','{','}']


password_list = []

for i in range(number1):
    num1 = random.choice(number)
    password_list .append(num1)

for i in range(letter1):
    lett = random.choice(letter)
    password_list.append(lett)

for i in range(symbol1):
    symb = random.choice(symbol)
    password_list.append (symb)


print(password_list)
random.shuffle(password_list)
print(password_list)

final_password =' '
for i in password_list:
    final_password = final_password + i

print(f"Your randomly generated password is: {final_password}")

