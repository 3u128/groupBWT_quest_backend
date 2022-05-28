#!/usr/bin/python

word = input("Type word, please: ")

lenght = len(word)
half = lenght // 2
j = 0
is_palindrom = True 

for i in range(half):
    j = j - 1
    if word[i] != word [j]:
        is_palindrom = False
        break

if is_palindrom:
    print(word, "is a palindrom")
else:
    print(word, "is not a palindrom")
