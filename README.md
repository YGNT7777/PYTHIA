# PYTHIA

![pythia](https://github.com/user-attachments/assets/70e0bda3-5a94-42e2-abe2-ba3224c2584a)

## DESCRIPTION
Our application is a desktop application with a graphical user interface. Its main purpose is to help investors make informed investment decisions using sentiment analysis from social media posts, such as Twitter (X) and Reddit. Additionally, our application performs risk analysis based on the percentage of positive, neutral, and negative posts. The user can maintain a watchlist of up to 5 items and track the price trends of the corresponding assets (cryptocurrencies, stocks, etc.) on their watchlist. Since cryptocurrencies and the stock market change at a rapid pace, our application also provides the user with daily email updates on the items in their watchlist.

The file requiers many personal and sensitive information. For obvious reasons it is not provided 
and the users have to take these information by their own. In the code is mentioned clearly where the information should be placed.
check files below:
  - 1.pyhtonia-d31d22a4d0a5.json
  - 2.code_for_server/credits.dat
  - 3.calc_handler.py
  - 4.main.py
  - 5.code_for_server/main.py
  - 6.code_for_server/scedule.py
  - 7.reddit_scraping.py

## LIBRARIES REQUIRED
- `pip install playwright`
run this in cmd --> `playwright install`
- `pip install schedule`
- `pip install PyQt6`
- `pip install Re`
- `pip install matplotlib`
- `pip install yfinance`
- `pip install gspread`
- `pip install pandas`
- `pip install oauth2client`
- `pip install datetime`
- `pip install vaderSentiment`
- `pip install praw`
- `pip install pandas`

### You can download the libraries by running

```bash
pip install requirements.txt
```

After you have install the requirements run:
```bash
playwright install
```

## HOW TO RUN

-1. You will need to go to reddit_scraping.py and add your data of your reddit account. ( You will nead to create your own reddit account)
-2. Then run the program normally

### If you want to also have a server.
-1. Go edit to calc_handler.py. On the url add 'YOUR_LINK_TO_GOOGLE_SPREADSHEETS'
-2. Go edit code_for_server/schedule.py and add on the variables username,pas and mail your information.
-3. Go edit code_for_server/main.py and on url add "YOUR_LINK_TO_GOOGLE_SPREADSHEETS"
-4. Run on code_for_server/main.py to run the server.

### In case you want to change the hour you receive the notifications from the server.
-1. Go to code_for_server/main.py
-2. On schedule.every().day.at("18:00").do(job) adjust the time as per your requirement



## Made by
- NIKOLAS NATSOS
- PETROS SAGIAKOS
- GEORGIOS LYMPITAKHS
- ERIKOS KOUTSOURHS
