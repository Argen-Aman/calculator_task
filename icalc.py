print('icalc is pleased to welcome you!')
while True:

    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    c = input('Sign (+, -, *, /): ')
    
    if c == '+':
        print('Answer is: ' + str(a + b))
    elif c == '-':
        print('Answer is: ' + str(a - b))
    elif c == '*':
        print('Answer is: ' + str(a * b))
    elif c == '/':
        if int(b) != 0:
            print('Answer is: ' + str(a / b))
        else:
            print('Are you kidding me? Did you ever get a primary school education? You can\'t divide by zero ;)')
    else:
        print('Incorrect sign!')

    d = input('To continue using me enter any key, to exit - print "exit" ')

    if d == 'exit': break
    else: a
print('Hope you enjoy it! Bye.')
