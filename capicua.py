import math

def capicua(number):
    number_str = str(number)
    length = len(number_str)
    i=0
    print(f"The lenght of the number/string is {length}")
    
    capicua = True 
    while capicua:
        
        if i == math.ceil(length/2):
            print('YOU FIND ONE CAPICUA !! \n')
            capicua = False
            break
            
        elif length%2 == 0 and number_str[i] == number_str[length-1-i]:
            i += 1
            
        elif length%2 != 0 and number_str[i] == number_str[length-1-i]:
            i += 1
        
        else:
            print('no capicua... \n')
            capicua = False
            break

check = True
while check:
    a = input('Put the number/string that you want to check: \n')
    capicua(a)
    b = input('Do you want to check another one, Y or N: \n')
    if b == 'n' or b == 'N':
        check = False
    else:
        check = True