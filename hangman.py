import random
import string
WORDLIST_FILENAME = "words.txt"

def load_words():  #extract words from wordfile
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("welcome to the game that decides your fate"); print("i choose from one of", len(wordlist), "words"); print("")
    return wordlist
def choose_word(wordlist): # choose random word from wordfile
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed): #checks if secret word obtained from guesses made till now
    seclist = list(secret_word)
    common = []
    for element in seclist:
        for element2 in letters_guessed:
            if element == element2:
                common.append(element)
    return len(common) == len(secret_word)
def get_guessed_word(secret_word, letters_guessed): #returns current status in form of a__l_
    seclist = list(secret_word)
    curstate = []
    for element in seclist:
        for element2 in letters_guessed:
            if element == element2:
                curstate.append(element); break

            if element2 == letters_guessed[-1]:
                curstate.append('_');

    curstring = ''.join(curstate)
    return curstring
def get_available_letters(letters_guessed): # returns unguessed letters from the alphabet
    alphabetstr = "abcdefghijklmnopqrstuvwxyz"
    alphabetlist = list(alphabetstr)
    for element in letters_guessed:
        alphabetlist.remove(element)

    remainingletters = ''.join(alphabetlist)
    return remainingletters

def hangman(secret_word):
    # At the start of the game, let the user know how many letters the secret_word contains and how many guesses s/he starts with.
    print("my word is" , len(secret_word), "letters long")
    print("you are deemed 6 guesses to escape your destiny")

    #  Before each round, you should display to the user how many guesses he has left and the letters that the user has not yet guessed.
    #  Ask the user to supply one guess per round. Remember to make sure that the user puts in a letter!

    letters_guessed = []
    invalidguesses = 0; hogayacheck = 0; noguesses = 6
    while noguesses>0 :
        if invalidguesses == 3:
          print("now you die"); break

        print("guesses remaining :",noguesses)
        curguess = input("enter guess...")

        for letter in letters_guessed:
          if letter == curguess:
            print("hogaya already"); noguesses = noguesses+1; hogayacheck = 1; break

        alphabets = "abcdefghijklmnopqrstuvwxyz"; alphabetlist = list(alphabets); alphabetlist.append(curguess); alphabetlist.remove(curguess); alphabetlistttt = list(alphabets)
        if alphabetlist ==  alphabetlistttt and hogayacheck == 0 :
                      print("i will say thid twice atmost, only letters man")
                      invalidguesses = invalidguesses+1; noguesses = noguesses+1

        elif len(curguess) != 1 and hogayacheck == 0 :
          if invalidguesses == 0 :
            print("i will say this twice atmost, only letters man")
          invalidguesses = invalidguesses+1; noguesses = noguesses+1

        # The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
        elif hogayacheck == 0:
          letters_guessed.append(curguess)
          for i in range(0,len(secret_word),1):
            if secret_word[i] == curguess:
              print("congrats");noguesses = noguesses+1; break
            if i == len(secret_word):
              print("one step closer to death") ; break

        hogayacheck = 0

        # After each guess, you should display to the user the partially guessed word so far.
        print(get_guessed_word(secret_word, letters_guessed))
        my_word = get_guessed_word(secret_word, letters_guessed)



        print("remaining letters :"+get_available_letters(letters_guessed))
        if is_word_guessed(secret_word, letters_guessed) == True:
          print("lucky guess... you will live today");return

        noguesses -= 1

    if is_word_guessed(secret_word, letters_guessed) == False:
          print("oops you are out of chances... ...now you die");return

# --------------------------------------------------------------------------------------------------------------------------------------------

def match_with_gaps(my_word, other_word):
    if len(my_word) != len(other_word):   #my_word and other_word are of the same length
        return len(my_word) == len(other_word)

    for idex in range(0,len(my_word),1):
        if my_word[idex] != "_" :
            if my_word[idex] != other_word[idex]:
                return my_word[idex] == other_word[idex]

    return True        #returns: boolean, True if all the actual letters of my_word match the  corresponding letters of other_word,
def show_possible_matches(my_word):
    #returns: nothing, but should print out every word in wordlist that matches my_word
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            print(other_word)
    return

def hangman_with_hints(secret_word):
    # At the start of the game, let the user know how many letters the secret_word contains and how many guesses s/he starts with.
    print("my word is", len(secret_word), "letters long")
    print("you are deemed 6 guesses to escape your destiny... type * for hints")

    #  Before each round, you should display to the user how many guesses he has left and the letters that the user has not yet guessed.
    #  Ask the user to supply one guess per round. Remember to make sure that the user puts in a letter!
    showvovels(secret_word)
    letters_guessed = []
    invalidguesses = 0;
    hogayacheck = 0;
    noguesses = 6
    while noguesses > 0:
        if invalidguesses == 3:
            print("now you die");
            break

        print("guesses remaining :", noguesses)
        curguess = input("enter guess...")

        if curguess == "*":
            show_possible_matches(my_word)
            noguesses = noguesses + 1


        for letter in letters_guessed:
            if letter == curguess:
                print("hogaya already");
                noguesses = noguesses + 1;
                hogayacheck = 1;
                break

        alphabets = "abcdefghijklmnopqrstuvwxyz";
        alphabetlist = list(alphabets);
        alphabetlist.append(curguess);
        alphabetlist.remove(curguess);
        alphabetlistttt = list(alphabets)
        if alphabetlist == alphabetlistttt and hogayacheck == 0 and curguess != "*":
            print("i will say this twice atmost, only letters man")
            invalidguesses = invalidguesses + 1;
            noguesses = noguesses + 1

        elif len(curguess) != 1 and hogayacheck == 0 and curguess != "*":
            if invalidguesses == 0:
                print("i will say this twice atmost, only letters man")
            invalidguesses = invalidguesses + 1;
            noguesses = noguesses + 1

        # The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
        elif hogayacheck == 0 and curguess != "*":
            letters_guessed.append(curguess)
            for i in range(0, len(secret_word), 1):
                if secret_word[i] == curguess:
                    print("congrats");
                    noguesses = noguesses + 1;
                    break
                if i == len(secret_word):
                    print("one step closer to death");
                    break

        hogayacheck = 0

        # After each guess, you should display to the user the partially guessed word so far.
        print(get_guessed_word(secret_word, letters_guessed))
        my_word = get_guessed_word(secret_word, letters_guessed)

        print("remaining letters :" + get_available_letters(letters_guessed))
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("lucky guess... you will live today");
            return

        noguesses -= 1

    if (is_word_guessed(secret_word, letters_guessed) == False):
        print("oops you are out of chances... ...now you die");
        return

def showvovels(secret_word):
    vovels = "aeiou"
    vovelslist = list(vovels)
    appearingvovels = ""
    for vovel in vovelslist:
        for letter in secret_word:
            if vovel == letter:
                appearingvovels = appearingvovels + vovel + " "
    print("vovels that appear are " + appearingvovels)

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
print("the answer was ",secret_word)
