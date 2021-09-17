import string
from words import choose_word
from image import IMAGES
import random

def is_word_guessed(secret_word, letters_guessed):
  if secret_word == get_guessed_word(secret_word, letters_guessed):
    return True
  else:
    return False

def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word

def ifValid(user_input):
  if len(user_input) != 1:
      return False

  if not user_input.isalpha():
      return False

  return True
def get_hint(secret_word, letters_guessed):
  letters_not_guessed = []
  index = 0
  while (index < len(secret_word)):
    letter = secret_word[index]
    if letter not in letters_guessed:
        if letter not in letters_not_guessed:
            letters_not_guessed.append(letter)

    index += 1

  return random.choice(letters_not_guessed)

def get_available_letters(letters_guessed):
    all_letters = string.ascii_lowercase
    letters_left= " "

    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left += letter
    
    return letters_left



def hangman(secret_word):
  name=input("enter your name: ")
  print(name)
  print ("Welcome to the game, Hangman!")
  print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
  j=0
  while j<1:
    user_difficulty_choice = input("Aap abhi kitni difficulty par yeh game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a, b, ya c ki terms mei batayein\n: ")
    total_lives = remaining_lives = 8
    images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]

    if user_difficulty_choice not in ["a", "b", "c"]:
      total_lives = remaining_lives = 8
      print("Aapki choice invalid hai.\nGame easy mode mei start kar rahe hai")

    elif user_difficulty_choice == "b":
      total_lives = remaining_lives = 6
      images_selection_list_indices = [0, 2, 3, 5, 6, 7]

    elif user_difficulty_choice == "c":
      total_lives = remaining_lives = 4
      images_selection_list_indices = [1, 3, 5, 7]
    j+=1   
  letters_guessed = []
  c=0
  while (remaining_lives > 0):
    available_letters = get_available_letters(letters_guessed)
    print ("Available letters: " + available_letters)

    guess = input("Please guess a letter: \n letter or hin ")
    letter = guess.lower()
      
    if letter=='hint':
      if c==0:
        print("your hint is: "+get_hint(secret_word, letters_guessed))
        c+=1
      else:
        print("You have used hint")
    if letter not in get_available_letters(letters_guessed):
      continue
    if(not ifValid(letter)):
      continue
    if letter in secret_word:
      letters_guessed.append(letter)
      print("Good guess: " + get_guessed_word(secret_word, letters_guessed))


      if is_word_guessed(secret_word, letters_guessed)==True:
        print(" * * Congratulations, you won! * * ")
        break
    else:
      print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
      print(IMAGES[images_selection_list_indices[total_lives-remaining_lives]]) ## <-- CHANGES HERE
      # letters_guessed.append(letter)
      remaining_lives -= 1
      print("Remaining Lives : ", remaining_lives)
      print(" ")
  else:
      print ("Your loss the game!!!______\n the word was", secret_word + get_guessed_word(secret_word, letters_guessed))
      letters_guessed.append(letter)
      
secret_word = choose_word()
print(secret_word)
hangman(secret_word)
