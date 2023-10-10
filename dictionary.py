#1a
#it is asking for every letter in a sentence and putting in a dictionarie and counts how many letters are there that are not recurring

#b
#it prints every letter

#c
#dictionarie

#d
# are the letter
#how many times it acurres

#e
#shorter way of doing it chars[char] = chars.get(char,0) + 1

#f
#.get it dos give the value and dos not end the code if there is not value

#g
'''
vowels = 'aeiouAEIOU'
sentence = input("Enter a sentence: ")
chars={}
for char in sentence:
    if char in vowels:
        if char in chars:
            chars[char]=chars[char]+1
        else:
            chars[char]=1
print(chars)
'''
#h

vowels = 'aeiouAEIOU'
sentence = input("Enter a sentence: ")
chars={}
for char in sentence:
    
    if char in vowels:
            chars['vowels']=chars.get('vowels',0) + 1
    else:
        chars['consonants']=chars.get('consonants',0) + 1
print(chars)

