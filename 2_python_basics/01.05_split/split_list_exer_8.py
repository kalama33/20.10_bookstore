

data = """id,first_name,last_name,email,ip_address
1,Jennine,Kohnert,jkohnert0@disqus.com,45.55.73.106
2,Katalin,Nolda,knolda1@123-reg.co.uk,223.30.112.215
3,Atalanta,Kaming,akaming2@gmpg.org,254.219.7.208
4,Kassie,Covell,kcovell3@cafepress.com,150.145.187.71
5,Vonni,Dignam,vdignam4@cafepress.com,138.219.98.53
6,Billie,Neubigging,bneubigging5@addthis.org,180.79.192.175
7,Etan,Peers,epeers6@cafepress.com,199.1.3.70
8,Pail,Walcher,pwalcher7@cafepress.com,199.170.155.126
9,Edlin,Kosel,ekosel8@columbia.edu,217.59.107.252
10,Jennifer,Tibalt,jtibalt9@sun.com,73.29.190.227
11,Douglas,Howe,dhowea@cafepress.com,93.94.19.71
12,Galina,Antoniewski,gantoniewskib@freewebs.com,69.177.160.104
13,Emelita,Pauer,epauerc@house.gov,178.243.169.131
14,Edmon,Cleugh,POTATOKING.2000@furl.net,100.219.252.98
15,kyo,zipulimakkarakeitto,kz@guardian.com,78.226.120.240
16,Harlin,Goodrich,hgoodrichf@guardian.com,232.242.92.122
17,Paddie,Brittain,pbrittaing@jigsy.com,230.116.80.29
18,Blisse,Barbrook,bbarbrookh@nytimes.com,153.237.126.205
19,Latia,Roughey,lrougheyi@guardian.co.uk,184.128.166.8
20,Gregoire,Castelow,gcastelowj@51.la,87.181.120.134
21,lorenza,kurn,ljurnk@nsw.gov.au,192.238.146.135
22,Dulciana,Wilce,dwilcel@noaa.gov,234.245.232.7
23,Boyd,Sponton,bspontonm@guardian.com,106.75.217.74
24,Lenora,Issard,lissardn@guardian.com,167.91.15.190
25,Lissi,Davidovitz,ldavidovitzo@guardian.com,48.7.220.5"""''

lines = data.split("\n") # Save the list of strings in a variable called `lines

#Count total numbers of users
print(data.split("\n")) # Split the string into a list of strings

print(len(lines)) # Print the amount of lines

# Print every 5th user. 
for i in range(5, len(lines), 5):
    print(lines[i])
    
    """
    print(lines[5])
    print(lines[10])
    print(lines[15])
    print(lines[20]) 
    print(lines[25])
    """

# Task 2 Print email address of each user

field = data.split(",")
print(field)

for field in lines[1:]: # We are skipping the line
    data = field.split(",")
    email = data[3]
    print(email)
    
#Task 3 endswith

co_uk_count = 0
for field in lines[1:]:
    email = field.split(",")[3]
    if ".co.uk" in email:
          co_uk_count += 1 
          
print(co_uk_count)


count = 0
name = field.split(',')[1]
second_name = field.split(",")[2]

if name.lower().startswith('k'):
        count += 1

if second_name.lower().startswith('k'):
        count += 1       

print(count)



