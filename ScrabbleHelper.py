from nltk.corpus import words
word_list = words.words()

print "Enter your characters here. If there is any guess word use '?' for that."
input_letters = raw_input()
#convert text to list of individual characters
input_letters_list = list(input_letters)
#number of ? (guess words) present in input
guess_words = input_letters_list.count("?")


res = []
for original in word_list:
    words = original
    #for all words having length greater than 1
    if len(words)>1:        
        
        for i in input_letters_list:
            if i in words:
                words = words.replace(i, "", 1)
        #if length of word is less than or equal to guess word, append in list
        if len(words)<=guess_words:
            
            res.append(original)
            
#sort list in desc order according to length of word
res.sort(key = lambda s: len(s), reverse = True)

for item in res:
    print item

