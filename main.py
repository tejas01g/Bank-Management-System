import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
                print("no such file exist")
    except Exception as err:
         print(f"an exception occured as {err}")



    def createaccount(self):
        data = {
             "name" : input("Tell your name :-"),
             "age" : int(input("Tell your age :-")),
             "email" : input("Tell your email"),
             "pin" : int(input("Tell your pin")),
             "accountNo." : 1234,
             "balance" : 0
        }
        if data['age'] < 18 or len(str(data['pin'])) != 4:
             print('sorry you cannot create your account')
        else:
             print("account has been created successfully")
             for i in data:
                  print(f"{i} : {data[i]}")
                  print("please note your account no.")


user = Bank()
print("press 1 for creating an account")
print("press 2 for Deposititing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

int(input("tell your response :-"))

if check == 1:
    user.Createaccount()