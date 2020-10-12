def reverse_words(sentence):
    new_sentence = ""
    sentence_array = sentence.split(" ")


    for word in sentence_array:
        new_word = ""

        for letter in word[::-1]:
            new_word += letter

        new_sentence += new_word + " "

    print(new_sentence)


sentence = "pass the salt please"
reverse_words(sentence)
