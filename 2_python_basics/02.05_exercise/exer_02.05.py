# Task 1

#Create a func named get user

from datetime import datetime

from datetime import date


date_of_birth = "%d-%B-%Y"

def get_user_age(date_of_birth):
    
birthdate = datetime.strptime(date_of_birth, "%d-%B-%Y").date()

    
    