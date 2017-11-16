# -*- coding: utf8 -*-
import random

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

def get_random_elements(my_list):

    rand_ele = random.randint(0, len(my_list) - 1)
    item = my_list[rand_ele]
    return item

user_answer = input("Tapez entrée pour découvrir une autre citation ou " +
                    "taper 'q' pour quitter le programme :")

while user_answer != "q":
    print(">>> {} a dit un jour : {}\n".format(get_random_elements(characters).capitalize(), get_random_elements(quotes)))
    
    user_answer = input("Tapez entrée pour découvrir une autre citation ou " +
                    "taper 'q' pour quitter le programme :\n")


