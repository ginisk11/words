
def print_upper_words(words,must_start_with):
    newWords=[]
    for word in words:
        if word[0] in must_start_with:
            newWords.append(word)
    converted_list = [x.upper() for x in newWords]
    print(converted_list)
    
    
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
