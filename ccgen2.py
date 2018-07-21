import random
print("Welcome to Random Australian ID Generator")
print(" ")
print("<----- Basic Details ----->")

fname = ['Sophia', 'Jackson', 'Emma', 'Aiden', 'Lucas', 'Liam', 'Ava', 'Mia', 'Noah', 'Isabella', 'Ethan', 'Riley', 'Mason', 'Aria', 'Caden', 'Zoe', 'Oliver', 'Charlotte', 'Elijah', 'Lily', 'Jacob', ]
lname = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'White', 'Martin', 'Anderson', 'Thompson', 'Nguyen', 'Turner', 'Walker', ]
secure_random = random.SystemRandom()
print("Name:", secure_random.choice(fname), secure_random.choice(lname))

stname = ['Alder', 'Browning', 'Guthrie', 'High', 'Druid', 'Main', 'Lockwood', 'Queen', 'MacKenzie', 'King', 'Mistletoe', 'First', 'Second', 'Third', 'Angas', 'Fosters', 'Regency', 'Newbon', 'Percy', 'Bruce', 'Pirie', 'Currie', 'Gilbert', 'Waymouth', 'Flinders', 'Turner', 'Melrose', 'Silver', 'Turnbull', 'Orana', 'Briens', 'Wright', 'Davies', ]
sttype = ['St', 'Rd', 'Ct', 'Ave', 'Ln', 'Cres']
secure_random = random.SystemRandom()
print("Address:", random.randint(1,75), secure_random.choice(stname), secure_random.choice(sttype),)

city = ['Adelaide, SA', 'Melbourne, VIC', 'Sydney, NSW', 'Perth, WA', 'Hobart, TAS', 'Brisbane, QLD', 'Surfers Paradise, QLD', 'Bendigo, VIC', 'Ballarat, VIC', 'Newcastle, NSW', 'Cairns, QLD', 'Townsville, QLD', 'Wollongong, NSW', 'Alice Springs, NT', 'Canberra, ACT', 'Darwin, NT', 'Toowoomba, QLD', 'Riverton, SA']
secure_random = random.SystemRandom()
print("City:", secure_random.choice(city))

print("Age:", random.randint(18,99))

print(" ")
print("<----- Credit/Debit Card ----->")
ccn = ['4448-8637-3225-7970', '4755-8490-8118-3724', '4019-1219-4794-6914', '4157-1447-4760-4063', '4188-9273-0003-7178']
secure_random = random.SystemRandom()
print("Credit Card Number:", secure_random.choice(ccn))

exp = ['08/24', '07/23', '04/21', '08/19']
secure_random = random.SystemRandom()
print("Expiry:", secure_random.choice(exp))

ccv = ['767', '816', '612', '912', '817', '827', '753', '621', '721', '562', '231']
secure_random = random.SystemRandom()
print("CCV:", secure_random.choice(ccv))

typ = ['Visa']
secure_random = random.SystemRandom()
print("Card Type:", secure_random.choice(typ))

bank = ['Australia and New Zealand Banking Group', 'Commonwealth Bank', 'National Australia Bank', 'Westpac', 'Bank of Melbourne', 'BankSA', 'Bank of Australia', 'ME Bank', 'ING Direct', 'AMP', 'Beyond Bank', 'Peoples Choice Credit Union', 'Suncorp Bank']
secure_random = random.SystemRandom()
print("Bank:", secure_random.choice(bank))

print(" ")
print("<----- Physical Infomation ----->")

bt = ['O-', 'O+', 'B-', 'B+', 'A-', 'A+', 'AB-', 'AB+']
secure_random = random.SystemRandom()
print("Blood Type:", secure_random.choice(bt))

print("Weight:", random.randint(32,90),"kg")