### SUBMITTED BY: PRANAY SINGHAL ###
### email: singhal.pranay@gmail.com ###

import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
#from subprocess import check_output
import seaborn as sns
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.corpus import wordnet
from nltk.corpus import state_union
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import words
import string
from collections import Counter
import collections, re
import pylab as plt


df = pd.read_csv(r'C:/Users/singh/Desktop/eluvio test/Eluvio_DS_Challenge.csv')
print(df)

###Print A wordcloud for the most probable words in the set###
word_string=" ".join(df['title'].str.lower())
wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white', max_font_size=250,width=2500, height=2500,
                      max_words=400).generate(word_string)
plt.clf()
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
wordcloud.to_file("C:/Users/singh/Desktop/eluvio test/img/ProbWordcloud.png")     #saving the image

###basic statistical analysis###

print(df.shape)
print(df['up_votes'].sort_values(ascending=False).value_counts().head(10))
print(df['down_votes'].sort_values(ascending=False).value_counts().head())
y = [x for x in df.sort_values('up_votes',ascending=False)['title'][:10]]
#print(y)
#[title for title in df.sort_values('up_votes', ascending=False)['title'][:10]]

# sns.set_style("dark")
# df.groupby('date_created')['up_votes'].mean().plot()
# df.groupby('date_created')['up_votes'].mean().rolling(window=120).mean().plot(figsize= (12, 4))
# #df.groupby('date_created').rolling(120)['up_votes'].mean().plot(figsize= (12, 4))
# sns.barplot(x='date_created',y='up_votes',data=df)
# plt.show()

#rolling mean of 120 days for the upvotes
df['rolling_avg'] = df['up_votes'].rolling(120).mean()
plt.figure(figsize = (12, 5))
sns.lineplot(x='date_created',y='rolling_avg',data=df,label='Upvotes per year')
plt.savefig("C:/Users/singh/Desktop/eluvio test/img/RollMeanVotes.png")
plt.show()


#top 15 Authors based on upvotes
attf= df.author.value_counts()[:15]
#print(attf)
attf.plot.bar(figsize= (10, 4))
plt.savefig("C:/Users/singh/Desktop/eluvio test/img/TopAuthor.png")
plt.show()
#Top 15 18+ stories from the data based on the upvotes
nsfwstory= df[df['over_18']== True]
nsfw=[story for story in nsfwstory.sort_values('up_votes', ascending=False)['title'][:15]]
for x in nsfw:
    print(x,end='\n')

#selected posts with more than 4500 votes
new_df=df[df.up_votes>4500]
print(len(new_df))
print(new_df.head(5))

#removing stopwords from the posts and using a word bag to collect all the remaining important words in the sentence
dict_filtered=new_df['title'].apply(lambda x: ' '.join([word for word in x.split() if word not in stopwords.words('english')]))
words_bag = [ collections.Counter(re.findall(r'\w+', txt)) for txt in dict_filtered]
sum_bags = sum(words_bag, collections.Counter())

#finding the proper nouns in the filtered bag
propnoun_list=pd.Series.to_string(dict_filtered)
tag_list = pos_tag(propnoun_list.split())
nnp_list = [word for word,pos in tag_list if pos == 'NNP']
nnp_countsum=Counter(nnp_list)


#taking top 45 pro noun words
top45 = nnp_countsum.most_common(46)
top45 = pd.DataFrame(top45)
print(top45)
top45 = top45.drop(top45.index[1]) #dropping 2nd element as it is just a Char
top45.rename(columns={0:'text',1:'score'},inplace=True)
top45_cloud = WordCloud(background_color='white',width=2000, height=2000).generate(' '.join(top45['text']))

#printing a wordcloud for the top 45 pronoun words
plt.figure(1,figsize=(8,8))
plt.imshow(top45_cloud)
plt.axis('off')
wordcloud.to_file("C:/Users/singh/Desktop/eluvio test/img/Top45Pronouns.png")
plt.show()


### Sentiment Analyzer using NLTK library ###
#finding avg for the top 45 pronouns and performing the sentimwnt analysis
senti=SentimentIntensityAnalyzer()
def sentimentAnalysis(wrd_list):
    global local_vars
    wrd_list_1=[wrd_list]   #creating a word list
    sent_bag = [sent for sent in dict_filtered if any(word in sent for word in wrd_list_1)]
    pol_score=[]    #polarity score list
    senti_val_list=[]
    for sentence in sent_bag:
        pol_score.append(senti.polarity_scores(sentence))
    senti_val_list = [i['compound'] for i in pol_score]
    senti_val =  sum(senti_val_list)/len(senti_val_list)

    #print(len(pol_score))
    senti_val_pos = filter(lambda pol_score: pol_score['compound']>0,pol_score)
    senti_val_neg = filter(lambda pol_score: pol_score['compound']<0,pol_score)
    return senti_val

###Plotting the graphs of sentiment score wrt the pronoun
top45_list = []
#print(senti_val)
top45['text'] = top45['text'].astype(str)
j = 0
for word in top45['text']:
    top45_list.append(sentimentAnalysis(word))
    j = j + 1
top45['senti_val'] = pd.Series(top45_list, index=top45.index)
Xaxis = np.arange(0,len(top45))
Yaxis=top45['senti_val']
labellist = top45['text']
ax=plt.bar(Xaxis,Yaxis, align='center', width=0.5)
#ax.autoscale(tight=True)
plt.xticks(Xaxis, labellist, rotation='vertical',fontsize=9)
plt.savefig("C:/Users/singh/Desktop/eluvio test/img/SentimentAnalyzer.png")
plt.show()

