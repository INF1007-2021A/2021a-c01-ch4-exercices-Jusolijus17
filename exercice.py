#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    nb_Caractères = 0

    for i in string :
        nb_Caractères += 1

    return (nb_Caractères % 2 == 0)


def remove_third_char(string: str) -> str:
    newString = string[0 : 2] + string[3:]
    return newString


def replace_char(string: str, old_char: str, new_char: str) -> str:
    newString = ""

    for letter in string :
        if letter != old_char :
            newString += letter
        else :
            newString += new_char

    return newString


def get_number_of_char(string: str, char: str) -> int:
    nbChar = 0

    for letter in string :
        if letter == char :
            nbChar += 1

    return nbChar


def get_number_of_words(sentence: str, word: str) -> int:
    words = str.split(sentence, " ")
    nbOccurrence = 0

    for word in words :
        if word.startswith("doo") :
            nbOccurrence += 1

    return nbOccurrence


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    chaine = "hello"
    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
