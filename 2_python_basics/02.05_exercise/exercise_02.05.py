# Task 1

#Create a func named get user

from datetime import datetime, date

def get_user_age(date_of_birth: str) -> int:
    date_of_b = datetime.now().strptime(date_of_birth, "%d-%m-%Y")
    current_date = datetime.now()
    age = (current_date - date_of_b).days / 365.2425
    
    return int(age)
    
def age_checker(age_of_user: int) -> int:
    if age_of_user < 18:
        print("\nYou need to be 18 years and above tocreate an account.\n")
        return 0
    elif age_of_user > 150:
        print("\nYou need to be 150 years or younger to create an account.\n")
        return 0
    else:
        print(f"\nYou are {age_of_user} years old, you can create anaccount\n")
        
attempts = 5 

while attempts > 0:
    date_of_birth = str(input("Enter the date of birth"))
    age = get_user_age(date_of_birth)
    
    if age_checker(age) == 1:
        get_user_info()
        break
    
    attempts -= 1
    
    
def get_user_info():
 