from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
'''this function takes as a parameter a list which contains the tweet text
and makes sentiment analysis in each text. It counts the positive, negative and neutral 
texts and then calculates each percentage. 
'''
def sentiment_vader(tweets):
    analyzer = SentimentIntensityAnalyzer()
    positive=0
    negative=0
    neutral=0
    compound=0
    #αναλύει το κάθε tweet
    for tweet in tweets:
        analyzer_attr = analyzer.polarity_scores(tweet)#creates the analyzer
        compound+=analyzer_attr['compound']
        if analyzer_attr['compound'] >= 0.5 :#biger than 0.5 counts as positive
            positive+=1
           
        elif analyzer_attr['compound'] <= - 0.5 :#smaller than -0.5 counts as negative
            negative+=1
        else:#the in betweens count as neutral
            neutral+=1
    #calculates the percentages
    percent_positive=(positive/len(tweets))*100
    percent_negative=(negative/len(tweets))*100
    percent_neutral=(neutral/len(tweets))*100
    comp_index=compound/len(tweets)
    return percent_positive, percent_negative, percent_neutral, comp_index
