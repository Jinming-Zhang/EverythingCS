import json
import numpy as np
f = open("model.json", "r")
model = json.load(f)


def predict_bayes(word):
    word = word.lower()
    num_spam_with_word = model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return 1.0*num_spam_with_word/(num_spam_with_word + num_ham_with_word)


def predict_naive_bayes(email):
    # numbers from the database
    total = 5728
    num_spam = 1368
    num_ham = total - num_spam
    # calculate the probability
    email = email.lower()
    words = set(email.split())
    spams = [1.0]
    hams = [1.0]
    # ignore the words that is not in the database
    for word in words:
        if word in model:
            spams_with_word = model[word]['spam']
            spams.append(spams_with_word/num_spam)  # *total)
            hams_with_word = model[word]['ham']
            hams.append(hams_with_word/num_ham)  # *total)
    # multiply the probability of each word appears in a spam/ham
    # to get the probability of all the words appear in a spam/ham
    prod_spams = (np.prod(spams)*num_spam)
    prod_hams = (np.prod(hams)*num_ham)
    # normalize the result
    return prod_spams/(prod_spams + prod_hams)


print(predict_naive_bayes("reed is a good student"))
