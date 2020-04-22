'''
Make a program which randomly chooses a number to guess and 
then the user will have a few chances to guess the number correctly.
In each wrong attempt, the computer will give a hint that the 
number is greater or smaller than the one you have guessed.
'''

# import random for randomly choosing number
import random

# # generate a random number btwn 1-100
# secret_number = random.randint(1,100)

# guess_limit = 5
# guess_count = 0

# print("Guess a number between 1 and 100. Enjoy")
# # Enable user to guess and check if it is right, if not repeat
# while guess_count < guess_limit:
#     try:
#         print('Enter guess')
#         guess = int(input(">>> "))
#         # Check if guess is the secret no
#         if guess == secret_number:
#             print('Congrations!!!')
#             print(f'The number is {secret_number}')
#             print(f"You guessed the number.")
#             break
#         elif guess > secret_number:
#             print('Please guess lower')
#         else:
#             print("Please guess higher")
#         # Increase value of guess_count by 1 only if the player entered a number
#         guess_count += 1
#         print(f"You have {guess_limit - guess_count} attempts remaining")
#     except KeyboardInterrupt:
#         print('Program Terminated')
#         break
#     except:
#         print("Invalid entry")


# # Check if no trials are remaining and the secret no is not guessed
# if guess_count == guess_limit and guess != secret_number:
#     print("Game Over")
#     print(f"The secret number was {secret_number}")



# Turning it into a function

def number_guess():
    '''
    Generates secret no, takes user guess and checks if it is correct.
    '''
    # generate a random number btwn 1-100
    secret_number = random.randint(1,100)

    guess_limit = 5
    guess_count = 0

    print("Guess a number between 1 and 100. Enjoy")
    
    # Enable user to guess and check if it is right, if not repeat
    while guess_count < guess_limit:

        try:
            print('Enter guess')
            guess = int(input(">>> "))
            # Check if guess is the secret no
            if guess == secret_number:
                print('Congrations!!!')
                print(f'The number is {secret_number}')
                print(f"You guessed the number.")
                break
            elif guess > secret_number:
                print('Please guess lower')
            else:
                print("Please guess higher")
            # Increase value of guess_count by 1 only if the player entered a number
            guess_count += 1
            print(f"You have {guess_limit - guess_count} attempts remaining")
        except KeyboardInterrupt:
            print('Program Terminated')
            break
        except:
            print("Invalid entry")

    # Check if no trials are remaining and the secret no is not guessed
    if guess_count == guess_limit and guess != secret_number:
        print("Game Over")
        print(f"The secret number was {secret_number}")

# if this program is run directly
if __name__ == "__main__":
    number_guess()