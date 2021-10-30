# In two words string, return 'True' if both words begin with same letter

def animal_crackers(text):
    word = text.lower().split()  # string.lower(): 소문자로
    # string.split(): seperate string by words
    return word[0][0] == word[1][0]

#string.capitalize() : change first character to capital
