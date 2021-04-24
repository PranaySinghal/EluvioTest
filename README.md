# EluvioTest
Private repository for Eluvio assessment (Data Scientist). 

# How to run the code?
A1) To run the python files, navigate EluvioTest/venv/Eluv.py and run the file "Eluv.py" with the required dependencies.    
A2) The sample output images are published in the EluvioTest/img folder.

B1) To run the Power BI file, navigate EluvioTest/Eluvio_Challenge.pbit and open the file using Microsoft Power BI.             
B2) If there system doesn't have Power BI, the published report can be access via the Eluvio_Challenge.pdf file (preferred option as the BI file may face errors due to data loading in the system)
# Model Description

The given problem statement provides a world news dataset with more than 500k datapoints along the lines of negative as well as positive news characterized based on the voting system (upvote/downvote). I have performed the tasks based on the given 3 techniques:
1. Statistical Analysis
2. Sentiment Analysis
3. Data Vizualization using Power BI

The 3 techniques are discussed briefly below:

1. Statistical Analysis

A) I have performed statistical analysis over the given data to find some basic features like top authors, top posts, and etc. 

<img src="https://user-images.githubusercontent.com/24355506/115950692-a9bed080-a491-11eb-9d8b-88f243e7c78c.PNG" height="400px" width="700px">
<img src="https://user-images.githubusercontent.com/24355506/115950698-acb9c100-a491-11eb-902b-840fff0c51d5.PNG" height="300px" width="300px">

B) The rolling mean of the posts based on a window of 120 days was performed on the dataset that gives us the analysis that the posts were more active as the timeline of date progressed.
 
<img src="https://user-images.githubusercontent.com/24355506/115951308-e9d38280-a494-11eb-97a6-d309130505ae.png" height="400px" width="800px">


C) Top 10 posts based on the upvotes:

['A biotech startup has managed to 3-D print fake rhino horns that carry the same genetic fingerprint as the actual horn. The company plans to flood Chinese rhino horn market at one-eighth of the price of the original, undercutting the price poachers can get and forcing them out eventually.', 'Twitter has forced 30 websites that archive politician s deleted tweets to shut down, removing an effective tool to keep politicians honest', '2.6 terabyte leak of Panamanian shell company data reveals  how a global industry led by major banks, legal firms, and asset management companies secretly manages the estates of politicians, Fifa officials, fraudsters and drug smugglers, celebrities and professional athletes. ', 'The police officer who leaked the footage of the surfers paradise police brutality, where the victims blood was washed away by officers, has been criminally charged for bringing it to the publics view. Officers who did the bashing get nothing.', 'Paris shooting survivor suing French media for giving away his location while he hid from shooters', 'Hundreds of thousands of leaked emails reveal massively widespread corruption in global oil industry', 'Brazil s Supreme Court has banned corporate contributions to political campaigns and parties', 'ISIS beheads 81-year-old pioneer archaeologist and foremost scholar on ancient Syria. Held captive for 1 month, he refused to tell ISIS the location of the treasures of Palmyra unto death.', 'Feeding cows seaweed could slash global greenhouse gas emissions, researchers say:  They discovered adding a small amount of dried seaweed to a cow s diet can reduce the amount of methane a cow produces by up to 99 per cent. ', 'Brazilian radio host famous for exposing corruption in his city murdered while broadcasting live on the air by two gunmen.']

D) Similarly, top posts based on the age criteria of 18+ or NSFW Posts, as the millenials like to call it, could be reviewed using the analysis.

"Armed suspect shot dead after trying to storm Paris police station"
"Syria Army killed over 200 ISIS militants in 3-day long offensive in Deir Ezzor"
"Man escapes ISIS execution"
"ISIS massacre 14 Real Madrid fans at supporters club in Baghdad"

2. Apart from this, I performed sentimental analysis using the NLTK library of python.

A) Word cloud with 400 max words with the highest probability was reviewed. As the cloud states, words like China, isis, USA, which were prominent in the dataset were displayed.

<img src="https://user-images.githubusercontent.com/24355506/115950289-387e1e00-a48f-11eb-8ac9-1436c93a4d2c.png" height="500" width="400">

B) Now I selected posts with more than 4500 votes. For these posts, removing stopwords from the posts and using a word bag to collect all the remaining important words in the sentence provided me with the dictionary which could be used for further sentiment analysis without any bogus or ambiguous words.The next step was to find the finding the proper nouns in the filtered bag after which I took top 45 pro noun words. 
Using this a wordcloud was visualized for the top 45 pronoun words according to the score.

<img src="https://user-images.githubusercontent.com/24355506/115952059-ea6e1800-a498-11eb-9622-8dbb72b7ba02.png" height="400" width="400">


C) Sentiment Analyzer using NLTK library: finding avg for the top 45 pronouns and performing the sentiment analysi using polarity scores            
D) Plotting the graphs of sentiment score with respect to the pronoun


<img src="https://user-images.githubusercontent.com/24355506/115952252-c3fcac80-a499-11eb-9d30-444774218aae.PNG" height="200" width="150">


<img src="https://user-images.githubusercontent.com/24355506/115952220-99125880-a499-11eb-95ec-08a40b74739d.png" height="370" width="750">


This analysis provides an analytical approach based on the characteristics and sentiments of the post. Using this, we could look into the positve and negative factor of the posts while providing basic analytical factors of the dataset. With the increasing use of social media, as the number of posts over the timeline graph suggested, the amount of data available for research as increased many folds which can be utilized in a special fashion to study behavioral as well as temporal patterns in the data. 

3. Keeping it in mind and having a knack for Data Visualization, I performed the analysis using Power BI tool as well which is a powerful analytical option in the growing industries and makes the tasks easier as well. The prepared dashboard can be accessed from the file on github while the preview can be viewed as a pdf from the pdf file uploaded on github.


Thank You.
