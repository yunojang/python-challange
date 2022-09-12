import random

rst_list = [
    '''
  | | | |/\       
  |_|_|_|\ \      
  |        /
  \_______/     
''', '''
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                           
''', '''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''
]

user_index = int(
    input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors. "))

print(rst_list[user_index])

com_index = random.randint(0, 2)

print("Computer chose:")
print(rst_list[com_index])


def rst(user, com):
    if user == com:
        return 'Draw'
    elif user == com + 1 or (user == 0 and com == 2):
        return 'Win'
    else:
        return 'lose'


print(f"You {rst(user_index, com_index)}")
