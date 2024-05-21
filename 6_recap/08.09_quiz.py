data = b'Hello, World!'
result = data.decode('ascii')
print(result)


data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21'
result = len(data)
print(result)

print("Hello".encode('ascii'))

data = b'Hello, World!'
with open('file.bin', 'wb') as f:
    f.write(data)
    
data = [72, 101, 108, 108, 111]
result = ''.join(chr(x) for x in data)

value = 10

def modify():
    value = 5
    value += 10

modify()
print(value)

count = 5

def increment():
    global count
    count += 10

increment()
print(count)


