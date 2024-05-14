from playwright.sync_api import sync_playwright
import time

'''
this piece of code is a class which has attributes user, password and email.
The class contains also a method that scrapes twitter (X) and returns a list with tweet text 
'''

class Scraper:
    def __init__(self,user,mail,pas):
        self.user=user
        self.mail=mail
        self.pas=pas
        self.browser = None
        self.page = None
        self.tweet_texts=[]
        '''
        the method below takes as parameters the keyword to be searched, 
        the count which identifies how many tweets will be extracted
        '''   
  
    def extract_tweets(self,key,count):
        with sync_playwright() as p:
            #launching playwright browser in headless mode
            self.browser = p.chromium.launch(headless=True, slow_mo=10)
            self.page = self.browser.new_page()
            
            self.page.goto("https://twitter.com/i/flow/login")
            #input username
            self.page.wait_for_selector("input[name=text]")
   
            self.page.fill("input[name=text]",self.mail)
            self.page.keyboard.press('Enter')
            #checking if redidercted to user validation
            self.page.wait_for_selector('H1[id="modal-header"]')
            heading=self.page.query_selector('H1[id="modal-header"]')
    
            if heading.inner_text()=="Εισαγάγετε τον κωδικό πρόσβασής σας" or heading.inner_text()=="Enter your password":
                self.page.wait_for_selector("input[name=password]")

                self.page.fill("input[name=password]",self.pas)
                self.page.keyboard.press('Enter')
                time.sleep(3)
                #entering twitter going to explore section
                link='https://twitter.com/search?q=%23'+key+'&src=typed_query'
                self.page.goto(link)
            else:
          
                self.page.wait_for_selector("input[name=text]")
                self.page.fill("input[name=text]",self.user)
                self.page.keyboard.press('Enter')
                
        
            
                #password input form
                self.page.wait_for_selector("input[name=password]")
    
                self.page.fill("input[name=password]",self.pas)
                self.page.keyboard.press('Enter')
            
            time.sleep(2)
            #entering twitter going to explore section
            self.page.wait_for_selector('input[placeholder="Search"]')
            sb=self.page.query_selector('input[placeholder="Search"]')
            key='#'+key
            sb.fill(key)
            #link='https://twitter.com/search?q=%23'+key+'&src=typed_query'
            #self.page.goto(link)
            
    
            time.sleep(2)
            #tweet extraction
       
            exit_cnt=0
            while len(self.tweet_texts)<count:
        
                self.page.wait_for_selector("div[data-testid='tweetText']")
                tweets = self.page.query_selector_all('div[data-testid="tweetText"]')

                for tweet in tweets:
                    #checks if the tweet already exists in the list
                    if tweet.inner_text() not in self.tweet_texts:
                        self.tweet_texts.append(tweet.inner_text())
                        exit_cnt=0
            
                exit_cnt+=1
                
                #checks if there are no more tweets
                if exit_cnt>30:
                    break
                #scrolls down the page
                self.page.mouse.wheel(0,15000)
            