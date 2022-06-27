import pandas as pd
import nltk
import gensim
from gensim import corpora,models,similarities
from Cluster import Cluster
import numpy
# nltk.download('punkt')
dataset = pd.read_csv('test.csv')
corpus = dataset['Comment'].values.tolist()
# Tokenize all the words in the corpus
tok_corp = [nltk.word_tokenize(sent) for sent in corpus]

model = gensim.models.Word2Vec(tok_corp,min_count=1)

p = []
data = model.wv.vectors
print(len( model.wv.vectors))
for i in data:
    p.append(i.tolist())
    #print(p[len(p)-1])

print(len(p))
print(type(p))
print(p[0])



print(model.wv.most_similar('physics'))

p  = numpy.array(p)

cluster = Cluster(data = p , cTarget=5 ,k =5)
print ("salmab")
cluster.fit()

print ("salma")


#min_count is the minimum time a word should appear in the dataset
#size is the size of the vector for each word

# Saving the model
#model.save('testmodel')
# Loading a saved model
#model = gensim.models.Word2Vec.load('testmodel')