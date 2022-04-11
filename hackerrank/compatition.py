def transformSentence(sentence):
    ls = sentence.split()
    result = []
    for i in ls:
        word = list(i)
        for letter in range(len(i) - 1):
            if word[letter + 1].lower() > word[letter].lower():
                word[letter + 1] = word[letter + 1].upper()
            elif word[letter + 1] > word[letter]:
                pass
            elif word[letter + 1].lower() == word[letter].lower():
                continue
            else:
                word[letter + 1] = word[letter + 1].lower()
        # result.join(word)
        result.append("".join(word))
    return(' '.join(result))


transformSentence("a Blue MOOn")

