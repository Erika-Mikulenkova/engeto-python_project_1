"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Erika Mikulenková
email: erika.mikulenkova@gmail.com
discord: Erika M.
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
separator = ("-" * 40)

# Přihlášení:
username = input("Enter username: ")
password = input("Enter password: ")

# Ověření přihlašovacího jména a hesla:
if user.get(username) == password:
    print(separator, 
          f"Welcome to the app, {username}.", "We have 3 texts to be analyzed.",
          separator,
          sep="\n")
          
else:
    print("Unregistered user, terminating the program...")
    quit()

# Výběr textu:
text_number = input("Enter a number btw. 1 and 3 to select: ")

if 1<= int(text_number) <=3 and text_number.isnumeric:
    print(separator)
    
else:
    print("Selected number is invalid. Terminating the program...")
    quit()

# Statistika textu:
text = TEXTS[int(text_number) - 1]
words = text.split()
clean_words = []

for word in words: 
    clean_words.append(word.strip(".,:;"))

number_words = len(clean_words)
print(f"There are {number_words} words in the selected text.")

title_words = []
upper_words = []
lower_words = []
num_words = []
num_sum = []

for word in clean_words:
# slova tvořená čísly:
    if word.isnumeric():
        num_words.append(int(word))

# první písmeno velké:
    elif word == word.title():
        title_words.append(word)
        
# slova velkými písmeny:
    elif word == word.upper():
        upper_words.append(word)
        
# slova malými písmeny:
    elif word == word.lower():
        lower_words.append(word)

# součet čísel:
num_sum = sum(num_words)

print(f"There are {len(title_words)} titlecase words.",
      f"There are {len(upper_words)} uppercase words.",
      f"There are {len(lower_words)} lowercase words.",
      f"There are {len(num_words)} numeric strings.",
      f"The sum of all the numbers {num_sum}.",
      sep="\n")

# Sloupcový graf:
print(separator, 
      f'{"LEN":>3}|{"OCCURENCES":^18}|{"NR."}',
      separator,
      sep="\n")

occurence_words = {}

for word in clean_words:
    if len(word) not in occurence_words:
        occurence_words[len(word)] = 1
    else:
        occurence_words[len(word)] = occurence_words[len(word)] + 1

sorted_dict = dict(sorted(occurence_words.items()))

for key, value in sorted_dict.items():
    print(f'{key:3}|{"*" * value:<18}|{value}')