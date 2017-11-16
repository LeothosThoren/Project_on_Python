# -*- coding: utf8 -*-
import random

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

def get_random_elements(my_list1, my_list2):

    rand_charac = random.randint(0, len(my_list1) - 1)
    rand_quote = random.randint(0, len(my_list2) - 1)
    item1 = my_list1[rand_charac]
    item2 = my_list2[rand_quote]
    return ">>> {} a dit un jour : {}\n".format(item1.capitalize(), item2)

user_answer = input("Tapez entrée pour découvrir une autre citation ou " +
                    "taper 'q' pour quitter le programme :")

while user_answer != "q":
    print(get_random_elements(characters, quotes))
    user_answer = input("Tapez entrée pour découvrir une autre citation ou " +
                    "taper 'q' pour quitter le programme :\n")


