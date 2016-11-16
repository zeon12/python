def censor(text, word):
    split = text.split()
    final = []
    for i in split:
        if i == word:
            final.append('*' * len(word))
        else:
            final.append(i)
    return " ".join(final)
