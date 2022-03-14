def anagrams(word, words):
    import copy
    answer =[]
    for i in words:
        word1 = list(copy.copy(word))
        if len(word)==len(i):
            for j in i:
                if j in word1:
                    word1.remove(j)
            if len(word1)==0:
                answer.append(i)
    return answer