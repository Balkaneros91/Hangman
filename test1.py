"""
Imports
"""
import random
import time
import os
import gspread
from google.oauth2.service_account import Credentials

words = [
    "mouse",
    "house",
    "love",
    "mississippi",
    "europe",
    "asia",
    "hangman",
    "game",
    "animal",
    "flower",
    "river",
    "yoghurt",
    "seed",
    "random",
    "lipstick",
    "surname",
    "playground",
    "python",
    "software",
    "object",
    "programming",
    "seaside",
    "city",
    "continent",
    "life",
    "positive",
    "school",
    "return",
    "spanish",
    "loyal",
    "rude",
    "mother",
    "siblings",
    "ocean",
    "atlantis",
    "americano",
    "aircraft",
    "holidays",
    "vacation",
    "institute",
    "care",
    "health",
    "human",
    "booking",
]

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]


class Hangman:
    """
    Hangman class
    """

    def __init__(self, max_wrong_guesses):
        """
        Method initializing Hangman object with attr and sets more attr's
        Set random word for game.
        """
        self.max_wrong_guesses = max_wrong_guesses
        self.word = random.choice(words)
        self.correct_letters = []
        self.incorrect_letters = []
        self.wrong_guesses = 0

    def play(self):
        """
        Play
        """
        while True:
            self.display_game_state()
            letter_or_word = input("Enter a letter or the whole word: \n")
            letter_or_word = letter_or_word.lower()
            if letter_or_word == self.word:
                self.correct_letters = list(self.word)
                self.display_game_state()
                print(
                    "You won in",
                    self.wrong_guesses,
                    "guesses! The word was:",
                    self.word,
                )
                break
            if len(letter_or_word) > 1:
                if letter_or_word == self.word:
                    self.correct_letters = list(self.word)
                    self.display_game_state()
                    print(
                        "You won in",
                        self.wrong_guesses,
                        "guesses! The word was:",
                        self.word,
                    )
                    break
                else:
                    if letter_or_word not in self.incorrect_letters:
                        self.incorrect_letters.append(letter_or_word)
                        self.wrong_guesses += 1
                    print("Incorrect guess! Please try again.")
                    time.sleep(2)
                    continue
            if not letter_or_word.isalpha() or len(letter_or_word) != 1:
                print("Error: Please enter a single letter.")
                time.sleep(2)
                continue
            if letter_or_word in self.correct_letters + self.incorrect_letters:
                print("Error: Already guessed letter.")
                print("Please try different letter.")
                time.sleep(2)
                continue
            if letter_or_word in self.word:
                self.correct_letters.append(letter_or_word)
                if all(c in self.correct_letters for c in self.word):
                    self.display_game_state()
                    print(
                        "You won in",
                        self.wrong_guesses,
                        "guesses! The random word is:",
                        self.word,
                    )
                    time.sleep(2)
                    break
            else:
                self.incorrect_letters.append(letter_or_word)
                self.wrong_guesses += 1
                if self.wrong_guesses >= self.max_wrong_guesses:
                    self.display_game_state()
                    print("You lost :( The word was:", self.word)
                    time.sleep(1)
                    break

        if game.wrong_guesses >= game.max_wrong_guesses:
            final_state = "lost"
        else:
            final_state = "won"

        result.append_row(
            [
                time.strftime("%Y-%m-%d"),
                username,
                game.word,
                game.wrong_guesses,
                final_state,
            ]
        )

    def display_game_state(self):
        """
        Game's visually displayed stages.
        """
        hangman_stages = [
            """
            +-------
            |/
            |
            |
            |
            |
          =====
            """,
            """
            +-------+
            |/
            |
            |
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |
            |
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |       I
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I\\
            |
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I\\
            |       o
            |
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I\\
            |       o
            |      /
          =====
            """,
            """
            +-------+
            |/      |
            |       Ö
            |      /I\\
            |       o
            |      / \\
          =====
            """,
            """
            +-------+
            |/      |
            |       X
            |      /I\\
            |       o
            |      / \\
          =====
            """,
        ]
        os.system("cls" if os.name == "nt" else "clear")
        print(hangman_stages[self.wrong_guesses])
        print("Word: " + " ".join([c if c in self.correct_letters
              else "_" for c in self.word]))
        print("Incorrectly guessed words:\n", self.incorrect_letters)
        print("Wrong guesses:", self.wrong_guesses, "/10")


if __name__ == "__main__":
    CREDS = Credentials.from_service_account_file("creds.json")
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("hangman_game")
    result = SHEET.worksheet("result")
    data = result.get_all_values()[1:]
    print("\nPrevious Game Results:")
    print("Date\t\tPlayer\tWord\tWrong Guesses\t\tResult")
    last_five_rows = data[-5:] if len(data) >= 5 else data
    for row in last_five_rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}\t\t{row[4]}")

    time.sleep(1)
    print("\nWelcome to Hangman World!")
    print("========================")
    time.sleep(1)
    print(
        r"""
          +----+
          |   \|
          Ö    |
         /|\   |
          |    |
         / \   |
             =====\n"""
    )
    while True:
        username = input("Enter your username: \n")
        username = username.strip()
        username = username.upper()
        if len(username) == 0 or username.isspace():
            print("This is not a valid name!")
            continue
        else:
            break
    time.sleep(1)
    print("\nHello {}. Wish you the best of luck! \n".format(username))
    time.sleep(1)
    print("HANGED or SAVED? Let's test your guessing skills =D \n")
    # time.sleep(1)
    PLAY_AGAIN = True
    while PLAY_AGAIN:
        game = Hangman(10)
        game.play()
        VALID_INPUT = False
        while not VALID_INPUT:
            restart = input("You want to play again ? (Y/N) \n >>> ")
            if restart in ["Yes", "yes", "Y", "y"]:
                PLAY_AGAIN = True
                VALID_INPUT = True
                print("Starting again... =D")
            elif restart in ["No", "no", "N", "n"]:
                PLAY_AGAIN = False
                VALID_INPUT = True
            else:
                print("Invalid input. Please enter (Y/N).")
                continue

            print("Thank you for playing. See You next time!")
