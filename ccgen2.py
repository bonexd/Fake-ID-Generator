# Imports
import random
import string
# All Possible Outcomes
# first name
fname = ['Sophia', 'Jackson', 'Emma', 'Aiden', 'Lucas', 'Liam', 'Ava', 'Mia', 'Noah', 'Isabella', 'Ethan', 'Riley', 'Mason', 'Aria', 'Caden', 'Zoe', 'Oliver', 'Charlotte', 'Elijah', 'Lily', 'Jacob', 'John', 'Lachlan', 'Georgia' ]
# last name
lname = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'White', 'Martin', 'Anderson', 'Thompson', 'Nguyen', 'Turner', 'Walker' ]
# street name
stname = ['Alder', 'Browning', 'Guthrie', 'High', 'Druid', 'Folland', 'Main', 'Lockwood', 'Queen', 'MacKenzie', 'King', 'Mistletoe', 'First', 'Second', 'Third', 'Angas', 'Fosters', 'Regency', 'Newbon', 'Percy', 'Bruce', 'Pirie', 'Currie', 'Gilbert', 'Waymouth', 'Flinders', 'Turner', 'Melrose', 'Silver', 'Turnbull', 'Orana', 'Briens', 'Wright', 'Davies', 'Church', 'Chapel', 'Hill', 'Robins']
# street type
sttype = ['St', 'Rd', 'Ct', 'Ave', 'Ln', 'Cres']
# city of residence
city = ['Adelaide, SA', 'Melbourne, VIC', 'Sydney, NSW', 'Perth, WA', 'Hobart, TAS', 'Brisbane, QLD', 'Surfers Paradise, QLD', 'Bendigo, VIC', 'Ballarat, VIC', 'Newcastle, NSW', 'Cairns, QLD', 'Townsville, QLD', 'Wollongong, NSW', 'Alice Springs, NT', 'Canberra, ACT', 'Darwin, NT', 'Toowoomba, QLD', 'Riverton, SA' 'Adelaide, SA', 'Melbourne, VIC', 'Sydney, NSW', 'Perth, WA', 'Adelaide, SA', 'Melbourne, VIC', 'Sydney, NSW', 'Perth, WA', 'Adelaide, SA', 'Melbourne, VIC', 'Sydney, NSW', 'Perth, WA', 'Brisbane, QLD', 'Brisbane, QLD', 'Brisbane, QLD']
# credit card number
ccn = ['4448-8637-3225-7970', '4755-8490-8118-3724', '4019-1219-4794-6914', '4157-1447-4760-4063', '4188-9273-0003-7178']
# credit card expiry month
expm = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# credit card expiry year
expy = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029']
# credit card provider
typ = ['Visa']
# bank
bank = ['Australia and New Zealand Banking Group', 'Commonwealth Bank', 'National Australia Bank', 'Westpac', 'Bank of Melbourne', 'BankSA', 'Bank of Australia', 'ME Bank', 'ING Direct', 'AMP', 'Beyond Bank', 'Peoples Choice Credit Union', 'Suncorp Bank']
# blood type
bt = ['O-', 'O+', 'B-', 'B+', 'A-', 'A+', 'AB+', 'AB-', 'O-', 'O+', 'B-', 'B+', 'A-', 'A+', 'AB+']
# medicare expiry month
medexpm = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# medicare expiry year
medexpy = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029']
# passport expiry month
pasexpm = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# passport expiry year
pasexpy = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029']
# passport issuing month
pasissm = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# passport issuing year
pasissy = ['2014', '2015', '2016', '2017', '2018' ]
# passport place of birth
paspob = ['North Adelaide', 'Modbury', 'Melbourne', 'Sydney', 'Brisbane', 'Perth', 'Darwin', 'Alice Springs', 'Gold Coast', 'Hobart', 'Cairns', 'Melbourne', 'Sydney', 'Melbourne', 'Sydney', 'Melbourne', 'Sydney']

# The Script
print("Welcome to Random Australian ID Generator")
print(" ")
print("<----- Basic Details ----->")
secure_random = random.SystemRandom()
print("Name:", secure_random.choice(fname), secure_random.choice(lname))
secure_random = random.SystemRandom()
print("Address:", random.randint(1,75), secure_random.choice(stname), secure_random.choice(sttype),)
secure_random = random.SystemRandom()
print("City:", secure_random.choice(city))
print("Age:", random.randint(18,68))
print(" ")
print("<----- Credit/Debit Card ----->")
secure_random = random.SystemRandom()
print("Credit Card Number:", secure_random.choice(ccn))
secure_random = random.SystemRandom()
print("Expiry:", secure_random.choice(expm), secure_random.choice(expy))
print("CCV:", random.randint(211,982))
secure_random = random.SystemRandom()
print("Card Type:", secure_random.choice(typ))
secure_random = random.SystemRandom()
print("Bank:", secure_random.choice(bank))
print(" ")
print("<----- Physical Infomation ----->")
secure_random = random.SystemRandom()
print("Blood Type:", secure_random.choice(bt))
print("Weight:", random.randint(45,90), "kg")
print("Height:", random.randint(140,168), "cm")
print(" ")
print("<----- ID Cards ----->")
print("<-- Medicare -->")
print("Medicare Number:", random.randint(3401,5923), random.randint(19223,72813), random.randint(1,4))
print("Medicare IRN:", random.randint(1,4))
secure_random = random.SystemRandom()
print("Medicare Expiry:", secure_random.choice(medexpm), secure_random.choice(medexpy))
print(" ")
print("<-- Passport -->")
print("Passport Number:", random.choice('NP'), random.randint(1927492,6927102))
secure_random = random.SystemRandom()
print("Passport Expiry:",random.randint(1,28), secure_random.choice(pasexpm), secure_random.choice(pasexpy))
secure_random = random.SystemRandom()
print("Passport Date of Issue:",random.randint(1,28), secure_random.choice(pasissm), secure_random.choice(pasissy))
secure_random = random.SystemRandom()
print("Passport Place of Birth:", secure_random.choice(paspob))
print(" ")
