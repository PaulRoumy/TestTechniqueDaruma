'''
Écrivez une fonction Python qui prend en entrée une chaîne de caractères et renvoie True si
la chaîne est un palindrome, False sinon.
Un palindrome est une chaîne qui reste identique lorsqu'elle est lue de gauche à droite ou
de droite à gauche, en ignorant la casse et les espaces.
Par exemple, "radar" et "A man a plan a canal Panama" sont des palindromes.
'''

def isPalindrome(word):
    reverseWord = word[::-1]
    if reverseWord == word:
        return True
    else:
        return False

myWord = input(("Entré un mot : "))
print(isPalindrome(myWord))
