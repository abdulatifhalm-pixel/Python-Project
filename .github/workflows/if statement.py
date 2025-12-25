hieght = int(input("Enter Hieght: "))
if hieght >= 3:
    print('you can ride')
    age = int(input("Enter Age: "))
    if age >= 12:
        bill = ('15')
        print('your bill is 150af')
    elif age >= 18:
        bill = ('25')
        print('your bill is 100af')
    else:
        bill = ('50')
        print('your bill is 500af')
    want_photo = input('do you want a photo?(y/n)')
    if want_photo == 'yes': 'y'
    bill = bill + 50
