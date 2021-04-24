# import numpy as np
# import pandas as pd
# from wordcloud import WordCloud, STOPWORDS
# import matplotlib.pyplot as plt
# from subprocess import check_output
# import seaborn as sns
# from nltk import word_tokenize
# from nltk.corpus import stopwords
# from nltk.tag import pos_tag
# from nltk.stem.porter import PorterStemmer
# from nltk.corpus import words
# import string
#
# df = pd.read_csv(r'C:/Users/singh/Desktop/eluvio test/Eluvio_DS_Challenge.csv')
# #print(df)
#
# ###Print A wordcloud for the most probable words in the set###
#
# #word_string=" ".join(df['title'].str.lower())
# # wordcloud = WordCloud(stopwords=STOPWORDS,
# #                           background_color='white', max_font_size=200,
# #                       max_words=300
# #                          ).generate(word_string)
# #plt.clf()
# #plt.imshow(wordcloud)
# #plt.axis('off')
# #plt.show()
# #wordcloud.to_file("img/first.png")     //saving the image
#
# ###basic statistical analysis###
#
# print(df.shape)
# #print(df['up_votes'].sort_values(ascending=False).value_counts().head(10))
# #print(df['down_votes'].sort_values(ascending=False).value_counts().head())
# y = [x for x in df.sort_values('up_votes',ascending=False)['title'][:10]]
# print(y)
#
# sns.set_style("dark")
# #df.groupby('date_created')['up_votes'].mean().plot()
# ##df.groupby('date_created')['up_votes'].mean().rolling(window=120).mean().plot(figsize= (12, 4))
# #sns.barplot(x='date_created',y='up_votes',data=df)
# #plt.show()
#
# #rolling mean of 120 days for the upvotes
# # df['rolling_avg'] = df['up_votes'].rolling(120).mean()
# # plt.figure(figsize = (12, 5))
# # sns.lineplot(x='date_created',y='rolling_avg',data=df,label='Upvotes per year')
# # plt.show()
#
# #top 15 Authors based on upvotes
# attf= df.author.value_counts()[:15]
# #print(attf)
# attf.plot.bar(figsize= (10, 4))
# #plt.show()
#
# #Top 15 18+ stories from the data based on the upvotes
# nsfwstory= df[df['over_18']== True]
# nsfw=[story for story in nsfwstory.sort_values('up_votes', ascending=False)['title'][:15]]
# # for x in nsfw:
# #     print(x,end='\n')
#
# [title for title in \
#      df.sort_values(by='up_votes', ascending=False)['title'].values[:10]]
#
# stopwords = set(stopwords.words('english'))
# best_titles = df.sort_values(by='up_votes', ascending=False)['title'].values[:10]
# best_words = set(np.concatenate([word_tokenize(t) for t in best_titles])) - stopwords
# best_words = {word.lower() for word in best_words}
# best_words = best_words - set(string.punctuation) - set(string.digits)
#
# #tokenization of title
# def is_float(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False
#
# best_words = {word for word in best_words if not is_float(word)}
# best_words = {word for word in best_words if "'" not in word}
# pd.Series(index=list(best_words)[:25], data=[(df[df['title'].map(lambda title: word in title)]['up_votes'].mean(),
#                                              df[df['title'].map(lambda title: word in title)]['up_votes'].count())
#                                             for word in list(best_words)[:25]])
#
# df[df['title'].map(lambda title: 'terabyte' in title)]
# words_tok=[[w.lower() for w in word_tokenize(t)] for t in df['title']]
# df['Tokenized_title']=words_tok
# all_words = pd.Series(np.concatenate(words_tok)).value_counts()
#
# #print(df.head(5))
#
# all_words = pd.Series(np.concatenate(words_tok)).value_counts()
# all_words = all_words[[word not in stopwords for word in all_words.index]]
# all_words = all_words[[word not in string.punctuation for word in all_words.index]]
# all_words = all_words[[word not in string.digits for word in all_words.index]]
# all_words = all_words[[not is_float(word) for word in all_words.index]]
# all_words = all_words[["'" not in word for word in all_words.index]]
# print(all_words[:10].index)
#
# stemmer = PorterStemmer()
# all_words.index = [stemmer.stem(w) for w in all_words.index]
#
# print(len(all_words))
# #all_words[:1000].plot()
# #plt.show()
#
# all_stems = all_words.groupby(by=all_words.index).sum().sort_values(ascending=False)
# all_stems[:10].index
# df['stemmed_title'] = df['tokenized_title'].map(lambda wl:[stemmer.stem(w) for w in wl])
#
# ###Most popular topics###
# print(pos_tag(df['Tokenized_title'][0]))
# df['pos_title'] = df['Tokenized_title'].map(lambda t: [t[1] for t in pos_tag(t)])
# print(df['pos_title'].head(5))
#
# def topicify(srs):
#
#     tags = srs['pos_title']
#     stems = srs['stemmed_title']
#     return [stem for (tag, stem) in zip(tags, stems) if tag in ['NN', 'NNS']]
#
# df['topics']=df.apply(topicify,axis='columns')
# print('working')
# print(df['topics'].head(10))
# topic_counts = pd.Series(np.concatenate(df['topics'].values)).value_counts()
# print(topic_counts.head(10))
# print(topic_counts[1:].head(10))
#
#
# topic_counts[1:].head(20).plot(kind='bar')
