#resturant_app# Python-Project
pizza = input("which kind of pizza do you want:s/M/L")
bill = 0
if pizza =="s":
    print ("small pizza price is 100af")
    bill+=100
    print(bill)
elif pizza == "m":
    print("medium pizza price is 150af")
    bill+=150
    print(bill)
elif pizza =="l":
    print("large pizza price is 200af")
    bill+=200
    print(bill)
else:
    print('please enter a valid answer')
cheese = input("do you want extra cheese y/n")
total_bill =0
if cheese == "y":
    print('extra cheese prise is 20af ')
    total_bill=bill+20
    print(total_bill)
else:
    print('thanks to follow us')
    total_bill=bill
    print(total_bill)
tea = input ("do you want tea y/n")
total_bill_= 0
if tea == "y":
    print('tea price is 30af')
    total_bill_=total_bill+30
    print(total_bill_)
else:
    print('thank you for for following us')
    print('have a good day')