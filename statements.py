"""is_hot = False
if is_hot:
    print("It's a hot day")
    print("drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")"""

"""
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
   print("Enjoy your day")
"""

"""
#program on having a good credit
price=1000000
has_good_credit = False
if has_good_credit:
    down_payment= 0.1 * price
else:
    down_payment=0.2*price
print(f"Down payment: ${down_payment}")
"""

"""
# if applicant has high income And good credit Eligible for Loan
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")

"""

"""
# if applicant has high income OR good credit Eligible for Loan    
has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for loan")
"""

"""good_credit = True
criminal_record = False
if good_credit and not criminal_record:
    print("Eligible for Loan")
"""

"""
temperature = 70
if(temperature > 30):
    print("it's a hot day")
elif(temperature < 10):
    print("it's a cold day")
else:
    print("it's neither hot nor cold")
"""
"""
name="Manasa"
if(len(name)<3):
    print("Name must be at least 3 characters.")
elif(len(name) > 50):
    print("Name must be a max of 50 characters.")
else:
    print("Name looks good!")
  """  
"""
#weight converter program
weight  = int(input('Weight: '))
unit = input('(L)bs or (k)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted = weight /0.45
    print(f"You are {converted} pounds")
"""
"""
i=1
while i <=10:
    print(i)
    i=i+1
print("Done")
"""
i=1
while i <=5:
    print('*' * i)
    i=i+1

    
