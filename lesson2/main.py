#def create_chess_field(size,color1='w',color2='b'):
#    chess_field=[]
#    for i in range(size):
#        middle_field=[]
#        for j in range(size):
#            if (i+j)%2 == 0:
#                middle_field.append(color2)
#            else:
#                middle_field.append(color1)
#        chess_field.append(middle_field)
#    print (chess_field)

#create_chess_field(4)
#create_chess_field(16)

# def calc(num1,num2,op='+'):
#    if op == '+':
#        a = num1 + num2
#    elif op == '-':
#        a = num1 - num2
#    elif op == '*':
#        a = num1 * num2
#    elif op == '/':
#        a = num1 / num2
#    return a

#print (calc (4,5))
#print (calc (4,5,'*'))
#from colorama import Fore
#print (Fore.BLUE,'Hello World!')

#from lesson2.functions import my_print
#my_print()

#import colorama
#import random

#def generate_password(length,case=False,special=False):
#    simple_chars='sdfbvdsfnbvafngbvadsfddhgwoerzmagndofgapkjkndfv'
#    case_chars='QWERTYUIOPASDFGHJKZXCVBNM'
#    special_chars='!@#$%^&%(){:"}>?'
#    chars = simple_chars
#    password = ''
#    if case:
#        chars+=case_chars
#    if special:
#        chars+=special_chars
#    for i in range(length):
#        password+=random.choice(chars)
#    return password
#print (colorama.Fore.CYAN,generate_password(8))
#print (colorama.Fore.RED,generate_password(10,True,True))

# def find_indexes(l,k):
#     for i in range(len(l)-1):
#         for j in range(len(l)):
#             if l[i]+l[j] == k:
#                 return i,j
#     return None
# print(find_indexes([1,2,3,4],6))

cortege=(1,2,4)

def replace(l,k,n):
    middle=l[k]
    l[k]=l[n]
    l[n]=middle
    l[k],l[n] =l[n],l[k] #тоже самое как и три строчки выше

def custom_print(*words): #звездочка - распаковка, то есть забрать всё
    for i in words:
        print(i)
custom_print(1,2,3)
