def anti_vowel(text):
    
    word = ""
    for t in text:
        if (t in "aeiouAEIOU") == False:
            word += t
    return word
