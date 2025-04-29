import numpy as np
import pandas
import json

emails = pandas.read_csv('./emails.csv')


def process_email(text):
    return list(set(text.split()))


# get all the words in the database into a unique set
emails['words'] = emails['text'].apply(process_email)

# a model that contains each word and its frequency in both ham and spam
model = {}
for index, email in emails.iterrows():
    for word in email['words']:
        if word not in model:
            model[word] = {'spam': 1, 'ham': 1}
        if word in model:
            if email['spam']:
                model[word]['spam'] += 1
            else:
                model[word]['ham'] += 1

# same trained model
trainedModel = json.dumps(model)
f = open("model.json", "w")
f.write(trainedModel)
f.close

# predict the probability of a single word


def predict_bayes(word):
    word = word.lower()
    num_spam_with_word = model[word]['spam']
    num_ham_with_word = model[word]['ham']
    return 1.0*num_spam_with_word/(num_spam_with_word + num_ham_with_word)


# predict all the words
def predict_naive_bayes(email):
    total = len(emails)
    num_spam = sum(emails['spam'])
    num_ham = total - num_spam
    email = email.lower()
    words = set(email.split())
    spams = [1.0]
    hams = [1.0]
    for word in words:
        if word in model:
            spams.append(model[word]['spam']/num_spam*total)
            hams.append(model[word]['ham']/num_ham*total)
    prod_spams = np.long(np.prod(spams)*num_spam)
    prod_hams = np.long(np.prod(hams)*num_ham)
    return prod_spams/(prod_spams + prod_hams)


print(predict_naive_bayes("Dear Jinming, TransUnion noted a change to your credit report. To find out the details simply click here to login to your account.  If you have any questions, please visit Customer Service for contact information and hours of service.  Thank you for choosing TransUnion to stay on top of your financial well-being!  TransUnion Get in the know"))
