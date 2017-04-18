import nltk
from nltk.probability import FreqDist, DictionaryProbDist, ELEProbDist, sum_logs

pos_tweets=[]
neg_tweets=[]


with open('./files/positive-words.txt') as fp:
    for line in fp:
        tuple = (line.rstrip(), 'positive')
        pos_tweets.append(tuple)
with open('./files/negative-words.txt') as fp:
    for line in fp:
        tuple = (line.rstrip(), 'negative')
        neg_tweets.append(tuple)


        
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3] 
    tweets.append((words_filtered, sentiment))
#print("TWEETS")
#print(tweets)
#print("================\n")

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    #print(wordlist.most_common(50))
    word_features = wordlist.keys()

    return word_features


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features



def train(labeled_featuresets, estimator=nltk.probability.ELEProbDist):
    # Create the P(label) distribution
    label_probdist = estimator(label_freqdist)
    # Create the P(fval|label, fname) distribution
    feature_probdist = {}

    return NaiveBayesClassifier(label_probdist, feature_probdist)



#print("Start")
word_features = get_word_features(get_words_in_tweets(tweets))
#print(tweets)
#print("\n")

training_set = nltk.classify.util.apply_features(extract_features, tweets)
#print(training_set)
#print("\n")
classifier = nltk.NaiveBayesClassifier.train(training_set)

#print(classifier)
#print("\n")
#print (classifier.show_most_informative_features(32))

tweet = 'You are such annoying person. but i still love you'
print (classifier.classify(extract_features(tweet.split())))