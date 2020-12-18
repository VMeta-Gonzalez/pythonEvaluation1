import random
import string

lettersAndNumbers = string.ascii_letters + string.digits

def generation():
    password = ''.join(random.choice(lettersAndNumbers) for x in range(11))
    print(f'Your automatically generated password is : {password}')


def askPass():
    query = input('Type "password" to generate a new password : ')
    if query == "password":
        generation()
    askPass()

askPass()