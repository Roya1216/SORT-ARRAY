number = int(input("How many numbers do you want to put in your array?"))


def appends(numbers):

    randomlist = []
    check = 0
    for i in range(0,numbers):
        new = float(input('please Enter your number : '))
        randomlist.append(new)
    while i < len(randomlist):
        if(randomlist[i] > randomlist[i - 1]):
           check = 1
        i += 1

    return check



if appends(number) == 1:
    
    print('yes')
else:
    print('no')