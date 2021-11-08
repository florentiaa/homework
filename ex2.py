words = ["xxx", "aaa", "r5t6yy", "g", "wow"]
def new_words(words):
    counter = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            counter += 1
    return counter

print(new_words(["xxx", "aaa", "r5t6yy", "g", "wow"]))