"""
Imports
"""
import gspread
from google.oauth2.service_account import Credentials

import words
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_game')

result = SHEET.worksheet('result')

data = result.get_all_values()
# print(data)

if __name__ == "__main__":
    time.sleep(1)
    print("\nWelcome to Hangman World!")
    print("========================")
    time.sleep(1)
    print('''
          +----+
          |   \|
          Ö    |
         /|\   |
          |    |
         / \   |
             =====\n'''
          )

    time.sleep(1)
    while True:
        player_name = input('Enter your name: ')
        player_name = player_name.strip()
        if len(player_name) == 0 or player_name.isspace():
            print("This is not a valid name!")
            continue
        break
    time.sleep(1)  
    print('\nHello {}. Wish you the best of luck! \n'.format(player_name))
    time.sleep(1)
    print('HANGED or SAVED? Let\'s test your guessing skills =D \n')