# Create a function to alternate the case of characters (upper and lower)
def alternate_case(str_sentence):
    result = ''
    for i in range(len(str_sentence)):
        if i % 2 == 0:
            result += str_sentence[i].upper()
        else:
            result += str_sentence[i].lower()
    return result

# Create a function to alternate the case of words (upper and lower)
def alternate_word_case(str_sentence):
    words = str_sentence.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    return ' '.join(words)

# Create a string sentence (I am learning to code)
str_sentence = "I am learning to code"

# alternate case of characters for output 'i Am lEaRnInG tO cOdE'
str_output_1 = alternate_case(str_sentence)
print(str_output_1)  

# alternate case of words for output 'i AM learning TO code'
str_output_2 = alternate_word_case(str_sentence)
print(str_output_2)  
