import os 
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class User_management:
    def __init__(self , first_name ,last_name ,email ,password ,status ="inactive"):
        self.first_name = first_name 
        self.last_name = last_name 
        self.email = email 
        self.password = password
        self.status =status 


    def display_users (self):
      print(f"First name :{self.first_name}")
      print(f"Last name :{self.last_name}")
      print(f"Email :{self.email}")
      print(f"Password :{self.password}")
      print(f"Status :{self.status}")
      print("_"*20)
      

def inputs_of_user():
    first_name =input("Enter the first name:")
    last_name = input("Enter the last name :")
    email =input("Entre the email :")
    password = input("Enter the password :")

    return User_management(first_name,last_name,email ,password)
new_users =[]
while True :
    
    print("\n\nWelcome to user management.....")
    print("1.Add new user:")
    print("2.Display all users :")
    print("3.Exit.....")

    chois_user =input("\n\nEnter your choice :")
    if chois_user == "1" :
        new_users.append(inputs_of_user())
        print("Users added successfully!")
        time.sleep(2)
        clear_screen()
    elif chois_user == "2" :
        clear_screen()
        if new_users :
            print("Display all new_users ............")
            time.sleep(2)
            for i in new_users :
                i.display_users()
            time.sleep(3)
            clear_screen()
            
        
        else:
            print("Sorry ,didn't find any user to display!")
            time.sleep(2)
            clear_screen()

    elif chois_user == "3":
        print("Exiting...........")
        break
    else:
        print("Please enter the number in list:")