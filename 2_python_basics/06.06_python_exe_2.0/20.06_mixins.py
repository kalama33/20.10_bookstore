# Create a a mixin called

class UserLenghtMixin:
#  The mixin should include a method called validate() that takes a value as an argument and checks if it meets certain criteria.   
    def validate(self, value): #validate func.
        # implement validation crit.
        return len(value) >= 5
        #if len(value) >= 5:
        #   return True
        #else:
        #   return False
        
# define usernamealpha.... 

class UserAlphanumericMixin:
    def validate(self, value):
        return value.isalnum()
        #if value.isalnum():
        #   return True
        #else:
        #    return False

# Create user class

class User:
    def set_username(self, username):
        if self.validate(username):
            self.username = username
            print("Username set")
            
        else:
            print("Invalid username.")
            
# create the new user with lenght val.

### Mixins ###

class UserWithLenghtValidation(User, UserLenghtMixin):
    """Validating the lenght of username"""
    pass

# create the new user with lenght val.

class UserWithAlphanumericValidation(User, UserAlphanumericMixin):
    """Validating the alphanum. of username"""
    pass

# create objects

user_1 = UserWithLenghtValidation()
user_1.set_username("alvaro")

user_2 = UserWithLenghtValidation()
user_2.set_username("pepe")

user_3 = UserWithAlphanumericValidation()
user_3.set_username("pepe1234")
    