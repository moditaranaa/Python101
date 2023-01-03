import getpass4

database= {
    "a" :1234,
    "b": "admin",
    "c": "none",

}

username= input("Enter username : ")
password = getpass4.getpass("Enter password : ")
for i in database.keys():
    if username == i:
        while password !=database.get(i):
            password = getpass4.getpass(" wrong password! Enter Password again : ")
            break
        print("You are successfully logged in!")

