# -*- coding: utf8 -*-
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero",
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def get_random_quote(my_list):
    #TODO
    item = my_list[0]
    return item

user_answer = input("Tapez entrée pour découvrir une autre citation ou " +
                    "taper 'B' pour quitter le programme :")

while user_answer != "B":
    print(get_random_quote(quotes))
    user_answer = input("Tapez entrée pour découvrir une autre citation ou " +
                    "taper 'B' pour quitter le programme :")

for character in characters:
   var =  character.capitalize()
   print(var)

print(get_random_quote(quotes))
