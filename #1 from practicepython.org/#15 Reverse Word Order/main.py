# Reverse Word Order


while True:
    def re_sentence():
        text = input("Enter a sentence: ")
        words = text.split()
        reversed_words = words[::-1]
        print(" ".join(reversed_words))

    re_sentence()
