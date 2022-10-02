import random


#A functions for calculate frequency of letters
def freq_cal(a_str):
    
    letters = [0]*26

    for i in range(len(a_str)):
        letters[ord(a_str[i].upper()) - 65] += 1

    return letters
    
#A functions to print winning word (As we have used color codes so we were facing problem to match the words for checking the result)
def win_random_word(a_str):

    win_random_word = ""

    for i in a_str:
        win_random_word += f'{green}{i}{reset}'
    
    return win_random_word

#Keyboard for checking if the letter is RED, GREEN or YELLOW
keyboard = ['  A ', ' B ', ' C ', ' D ', ' E ', ' F ',
            ' G ', ' H ', ' I ', ' J ', ' K ', ' L ',
            ' M ', ' N ', ' O ', ' P ', ' Q ', ' R ',
            ' S ', ' T ', ' U ', ' V ', ' W ', ' X ',
            ' Y ', ' Z ']

#Color codes to print colored text
green = '\033[1;30;42m '
yellow = '\033[1;30;43m '
red = '\033[1;30;41m '
reset = ' \033[0;0m'

# I've choosen 25 random words from the upper list with a for loop.
word_list = ['smart', 'brain', 'apply', 'extra', 'acute',
             'money', 'going', 'title', 'steam', 'three',
             'shirt', 'basis', 'worry', 'spoke', 'cream',
             'built', 'noted', 'every', 'youth', 'trial',
             'cross', 'store', 'those', 'chart', 'fixed']

#Random word from the Word List
random_word = word_list[random.randint(1, len(word_list)-1)].upper()

#Colored random word from the function of print winning word
win_random_word = win_random_word(random_word)

#Frequency of letters of random word
random_freq = list(freq_cal(random_word))

#Main logic of the game
attemps = 0
won = False

while attemps < 6:

    print_word = ""
    user_word = input("Enter a 5 letter word: ").upper()
    user_freq = list(freq_cal(user_word))

    if len(user_word) == 5:
            
            for i in range(5):
              
                if random_word[i] == user_word[i]:
                    print_word += f'{green}{user_word[i].upper()}{reset}'
                    keyboard[ord(user_word[i])-65] = f'{green}{user_word[i].upper()}{reset}'
                elif user_word[i] in random_word:
                    if user_freq[ord(user_word[i]) - 65] > random_freq[ord(user_word[i]) - 65]:
                        user_freq[ord(user_word[i]) - 65] -= 1
                        print_word += f'{red}{user_word[i].upper()}{reset}'
                    elif user_freq[ord(user_word[i]) - 65] < random_freq[ord(user_word[i]) - 65]:
                        random_freq[ord(user_word[i]) - 65] -= 1
                        print_word += f'{red}{user_word[i].upper()}{reset}'
                    elif user_freq[ord(user_word[i]) - 65] == random_freq[ord(user_word[i]) - 65]:
                        print_word += f'{yellow}{user_word[i].upper()}{reset}'
                        keyboard[ord(user_word[i])-65] = f'{yellow}{user_word[i].upper()}{reset}'
                else:
                    print_word += f'{red}{user_word[i].upper()}{reset}'
                    keyboard[ord(user_word[i])-65] = f'{red}{user_word[i].upper()}{reset}'
        
            print(print_word)

            print("========= KEYBOARD ========")

            for i in range(1, len(keyboard)+1):
                if i % 7 == 0:
                 print(keyboard[i], end="\n")
                else:
                  print(keyboard[i-1], end=" ")

            print()
            print("===========================")
            print()

            if print_word == win_random_word:
                won = True
                break

            attemps += 1

    else:
        print(f'{red}You are only allowed to enter a 5 letter word!{reset}')
        won = None
        break

#Checking loss or win
if won == True:
    print(f'{green}Congratulations! You have won the game in {attemps+1} attemps.{reset}')
elif won == False:
    print(f'{red}You lost! Try again.{reset}')
