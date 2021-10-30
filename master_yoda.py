#return list of words to a setence with the words reversed
#in order to change list to string - use .join() method



def master_yoda(text):
    textlist = text.split()  #split string by words
    textlist = textlist[::-1]  #reverse words order
    return ' '.join(textlist)  #connect words with ' ' to string

print(master_yoda('I am home'))