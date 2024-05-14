import schedule
import time
from scedule import send_mail
import pandas as pd
import datetime 


def job():
    url="YOUR_LINK_TO_GOOGLE_SPREADSHEETS"
    df=pd.read_csv(url)
    check_date(df)

def check_date(df):
    x=datetime.datetime.now()
    today=x.strftime("%A")
    for _, row in df.iterrows():
        if row['send']=='yes':
            send_mail(row['email'])

# Schedule the job to run every day at a specific time
schedule.every().day.at("18:00").do(job)  # Adjust the time as per your requirement

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check for scheduled jobs every 60 seconds
