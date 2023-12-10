import csv

csv_file='login.csv'


def register():
    with open("login.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        user_name=input("enter your user_name:")
        email = input("Enter your email: ")
        password = input('Enter the password: ')
        password_2 = input('Re-type password: ')
        if password == password_2:
            writer.writerow([email, password])
            print("Registration is successful!")
        else:
            print("Please try again.")
    return user_name,email,password_2            

def login(user_name,password):
 
    with open("login.csv", mode='r') as f:  
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [user_name, password]:
                print("You are logged in!")
                return True
        print("Please try again!")
        return False
register()
user_name= input("Please enter email: ")
password = input("Please enter your password: ")
result = login(user_name,password)
print(result)
