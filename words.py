words = [
    'mouse',
    'house',
    'love',
    'mississippi',
    'europe',
    'asia',
    'hangman',
    'game',
    'animal',
    'flower',
    'river',
    'yoghurt',
    'seed',
    'random',
    'lipstick',
    'surname',
    'playground',
    'python',
    'software',
    'object',
    'programming',
    'seaside',
    'city',
    'continent',
    'life',
    'positive',
    'school',
    'return',
    'spanish',
    'loyal',
    'rude',
    'mother',
    'siblings',
    'ocean',
    'atlantis',
    'americano',
    'aircraft',
    'holidays',
    'vacation',
    'institute',
    'care',
    'health',
    'human',
    'booking'
]

def display_game_state(self):
    """
    Stages for the wrongly guessed letters
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
            """            
        ]
  
print(words)
hangman_stages = display_game_state()
print(hangman_stages)