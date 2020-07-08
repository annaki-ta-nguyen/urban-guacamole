#ask for user's full name and birthday
name = input("Enter your FULL name: ")
birthday = input("Enter your birthday (DD/MM/YYYY): ")

#A: Calculate life path number
def generate_list(birthday):
  birthday_list = []
  for x in range(len(birthday)):
    if birthday[x].isdigit() == True:
      birthday_list.append(int(birthday[x]))
  return birthday_list

birthday_list = generate_list(birthday)

def calc_lifepath(birthday_list):
  lifepath_number = 0
  for y in range(len(birthday_list)):
    lifepath_number += birthday_list[y]
    while lifepath_number > 9:
      string1 = str(lifepath_number)
      lifepath_number = 0
      for z in range(len(string1)):
        lifepath_number += int(string1[z])
  return lifepath_number

lifepath_number = calc_lifepath(birthday_list)
print("Your life path number is: {0}.".format(lifepath_number))

#B: Calculate destiny number
def generate_name_list(name):
  name_list = []
  for x in range(len(name)):
    if name[x] in ['a', 'A', 'J', 'j', 'S', 's']:
      name_list.append(1)
    elif name[x] in ['B', 'K','T', 'b', 'k', 't']:
      name_list.append(2)
    elif name[x] in ['C', 'L','U', 'c', 'l', 'u']:
      name_list.append(3)
    elif name[x] in ['D', 'M','V', 'd', 'm', 'v']:
      name_list.append(4)
    elif name[x] in ['E', 'N','W', 'e', 'n', 'w']:
      name_list.append(5)
    elif name[x] in ['F', 'O','X', 'f', 'o', 'x']:
      name_list.append(6)
    elif name[x] in ['G', 'P','Y', 'g', 'p', 'y']:
      name_list.append(7)
    elif name[x] in ['H', 'Q','Z', 'h', 'q', 'z']:
      name_list.append(8)
    elif name[x] in ['I', 'R', 'i', 'r']:
      name_list.append(9)
  return name_list

name_list = generate_name_list(name)

def calc_destiny(name_list):
  destiny_number = 0
  for n in range(len(name_list)):
    destiny_number += name_list[n]
  while destiny_number > 9:
    string2 = str(destiny_number)
    destiny_number = 0
    for m in range(len(string2)):
      destiny_number += int(string2[m])
  return destiny_number

destiny_number = calc_destiny(name_list)
print("Your destiny number is: {0}".format(destiny_number))

#C: Calculate personality number
def generate_cons_list(name):
  cons_list = [] #consonants in name
  for x in range(len(name)):
    if (x == 0 and (name[x] == 'Y' or name[x] == 'y')) or (x != 0 and name[x - 1] == ' ' and (name[x] == 'Y' or name[x] == 'y')):
      cons_list.append(7)
    if name[x] in ['J', 'j', 'S', 's']:
      cons_list.append(1)
    elif name[x] in ['B', 'K','T', 'b', 'k', 't']:
      cons_list.append(2)
    elif name[x] in ['C', 'L', 'c', 'l']:
      cons_list.append(3)
    elif name[x] in ['D', 'M','V', 'd', 'm', 'v']:
      cons_list.append(4)
    elif name[x] in ['N','W', 'n', 'w']:
      cons_list.append(5)
    elif name[x] in ['F','X', 'f', 'x']:
      cons_list.append(6)
    elif name[x] in ['G', 'P', 'g', 'p']:
      cons_list.append(7)
    elif name[x] in ['H', 'Q','Z', 'h', 'q', 'z']:
      cons_list.append(8)
    elif name[x] in ['R', 'r']:
      cons_list.append(9)
  return cons_list

cons_list = generate_cons_list(name)

def calc_personality(cons_list):
  personality_number = 0
  for n in range(len(cons_list)):
    personality_number += cons_list[n]
  while personality_number > 9:
    string3 = str(personality_number)
    personality_number = 0
    for m in range(len(string3)):
      personality_number += int(string3[m])
  return personality_number

personality_number = calc_personality(cons_list)
print("Your personality number is: {0}".format(personality_number))

#D: Calculate soul urge number

def generate_vowel_list(name):
  vowel_list = []
  for x in range(len(name)):
    if x != 0 and name[x-1] != ' ' and (name[x] == 'Y' or name[x] == 'y'):
      vowel_list.append(7)
    if name[x] in ['a', 'A']:
      vowel_list.append(1)
    elif name[x] in ['U', 'u']:
      vowel_list.append(3)
    elif name[x] in ['E', 'e']:
      vowel_list.append(5)
    elif name[x] in ['O','o']:
      vowel_list.append(6)
    elif name[x] in ['I', 'i']:
      vowel_list.append(9)
  return vowel_list

vowel_list = generate_vowel_list(name)

def calc_soul(vowel_list):
  soul_number = 0
  for n in range(len(vowel_list)):
    soul_number += vowel_list[n]
  while soul_number > 9:
    string4 = str(soul_number)
    soul_number = 0
    for m in range(len(string4)):
      soul_number += int(string4[m])
  return soul_number

soul_number = calc_soul(vowel_list)
print("Your soul urge number is: {0}".format(soul_number))