# EluvioTest
Private repository for Eluvio assessment (Data Scientist). 


#print(df['down_votes'].sort_values(ascending=False).value_counts().head())
y = [x for x in df.sort_values('up_votes',ascending=False)['title'][:10]]
print(y)
