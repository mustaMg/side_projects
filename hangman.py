from sympy import Q


HANGMANPICS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]
word = "winners"

status = ["_"] * len(word)

guessed = []
true_guessed = []
guess_count = 0
while guess_count < len(word) or len(true_guessed) < len(status):
    try:
        ask = input("Please guess a letter or whole word: ")
        guessed.append(ask)
        if ask.isalpha():
            if ask in word:
                found = [pos for pos, char in enumerate(word) if char == ask]

                if ask not in true_guessed:
                    for i in found:
                        status[i] = ask
                        true_guessed.append(ask)
                        print(ask)
                elif ask in true_guessed or ask in guessed:
                    print("Already used this letter!")
                    continue
                if ask == word:
                    print(f"{'*'*25}\n*\t YOU WIN!\t*\n{'*'*25}")
                    break
                print(guessed, word)
                print(true_guessed)
                if len(true_guessed) == len(status) or guessed[0] == word:
                    print(f"{'*'*25}\n*\t YOU WIN!\t*\n{'*'*25}")
                    break
                continue

            else:
                print(HANGMANPICS[guess_count])
                guess_count += 1
                continue

        else:
            print("Sorry, only letter or word acceptable")
            continue
    except ValueError:
        print("Sorry, guess is not valid")
        continue
