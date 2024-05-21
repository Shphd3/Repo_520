mode = input("Choose your mode: " + '\n'
             "1. pt" + '\n'
             "2. inch" + '\n')

if mode == '1':
    pt = eval(input("Please input pt size: "))
    print('inch = ',float(pt) / 72)

elif mode == '2':
    inch = eval(input('Please input inch size: '))
    print('pt = ', float(inch) * 72)
else:
    print('Fail!')
