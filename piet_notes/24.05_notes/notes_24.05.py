### Closures

def make_averager():
    series = []
    
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    
    return averager    # averager is a function

avg = make_averager() # what type is avg?
print(avg)
print(avg(10))
print(avg(1))