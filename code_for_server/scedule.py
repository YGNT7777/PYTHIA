import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
from t_scraper2 import Scraper
import sentiment
from risk_counter import risk_analyzer
import pandas as pd

'''this code file makes a sentiment analysis by importing 
and using the other files such us the t_scraper_2, the sentiment and the risk.
There is a feature in which user has the ability to have a watch list of assets.
Our app notifies him via email weekly (every monday) using schedule and smtplib libraries.
'''   

def send_mail(email_receiver):
        #credetials for the x_scraper
    
    username="YOUR_USERNAME_IN_TWITTER"

    pas="YOUR_PASSWORD_IN_TWITTER"

    mail="yOUR_EMAIL_IN_TWITTER"

    #creating a Scraper object
    x_scrape=Scraper(username,mail,pas)

    #opens the watch list file
    
    url="https://docs.google.com/spreadsheets/d/1ctWjDCcINCa-1UxTsOYJ7e2JEFRl70EMp4BDVaPsIZs/gviz/tq?tqx=out:csv&sheet=pythonia"

    df=pd.read_csv(url)
    print(df)

   
    wl=[]
    for _, row in df.iterrows():#reads all the rows
        if email_receiver==row['email']:#finds the user to send the email an reads his watchlist
            wl.append(row['item1'])
            wl.append(row['item2'])
            wl.append(row['item3'])
            wl.append(row['item4'])
            wl.append(row['item5'])
    wl_cleaned=[]
    for i in wl:#cleans the wtachlist
        try:
            if i.lower()!='nan':
                wl_cleaned.append(i)
           
        except:
            pass
        
    try:
        
        #for every item in the watclist
        #does the below tasks
       
        for item in wl_cleaned:
            #extracting tweets
            x_scrape.extract_tweets(item,50)

            #  sentiment analysis part
            positive,negative,neutral,comp_index=sentiment.sentiment_vader(x_scrape.tweet_texts)

            #risk analysis
            risk=risk_analyzer(positive,negative,neutral)
            risk.risk_taken()
        
            
            sender='THE_EMAIL_THAT_CORESPONDS_TO_THE_APP_PASSWORD_IN_CREDITS_FILE'
            #the sender
    
            #reading credits
            creds=open('credits.dat','r')
            password=creds.readline()
            #creating the smtp server
            smtp_conn=smtplib.SMTP("smtp.gmail.com",587)

            #securing conection with ttls
            smtp_conn.starttls()

            #login phase
            smtp_conn.login(sender,password)
        
            #creating message

            message = MIMEMultipart("alternative")
            message["Subject"] = 'Notification from Pythia Investments'
            message["From"] = sender
            message["To"] = email_receiver
            #html format
            html_content = f'''
                <html>
                    <body>
                        <p>Hi, I hope you are okay</p>
                        <p>check on the risk results bellow for <strong>{item}</strong></p>
                        <table style="width:100%" border="1px solid black">
                            <tr>
                                <td>positive</td>
                                <td>{positive}</td>
                            </tr>
                            <tr>
                                <td>negative</td>
                                <td>{negative}</td>
                            </tr>
                            <tr>
                                <td>neutral</td>
                                <td>{neutral}</td>
                            </tr>
                            <tr>
                                <td>overall risk</td>
                                <td>{risk.risk}</td>
                            </tr>
                        </table>
                    </body>
                </html>'''
    
            html_part = MIMEText(html_content, "html")
            message.attach(html_part)
            #send the email
            smtp_conn.sendmail(sender,email_receiver,message.as_string())

            smtp_conn.quit()
    except:
        print('error')
   
    
