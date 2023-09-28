import random

# Lista de palabras predefinidas
words = ["Python", "Programming", "Computer", "Algorithm", "Development","Variable", "Condition", "Loop", "Function", "Class","Object", "Interface", "Library", "Array", "String","Number", "Logic", "Debugging", "Comment", "Framework"]

# Luego puedes comenzar a jugar con la palabra secreta

def select_word():
    secret_word = random.choice(words)
    return secret_word
