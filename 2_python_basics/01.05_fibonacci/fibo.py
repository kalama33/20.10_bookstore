#fibonacci

prev = 1
prevprev = 0
current = 1

for i in range(50): # i for index or int.
    print(prev)
    prevprev = prev
    prev = current
    current = prev + prevprev
    
    