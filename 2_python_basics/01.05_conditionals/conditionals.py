my_name = input("What is your name? ")
my_age = int(input("How old are you? ")) # Cast the result of input to an integer

if (my_age <= 17):
    
#Check the name

    if (my_name == "Veera"): #Indentetion is critical # Conditional statement
        print("Hi Veera")    #Equal equal
        print("Looking goof!")
        score = 10
        
    elif(my_name == "Rauli"):
        #Indentetion is critical  
        #Indentetion creates a section or sequence of code
        print("Hey Rauli")
        score = 99

    else:
        print("Who are you even?")
        score = 3

    print("Score: ", score)
    
else:
    print("Nope. Just for kidz!")    

