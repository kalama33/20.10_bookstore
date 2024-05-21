try:
    with open("/home/dci-student/python/recap/18.09_exeptions/numbers.txt", "r") as file:
        total = 0
        
        for line in file:
            try:
                number = float(line.strip())
                total += number
            except ValueError:
                print("Invalid number found.")
                
    print("Sum of numbers:", total)
    
except FileNotFoundError:
    print("File not found.")