import pandas as pd
import gspread # google spreadsheet libraries
from oauth2client.service_account import ServiceAccountCredentials

import datetime

def no_send(): #updates spreadsheet with 'no'
    flag=0
    try:
        with open('assets/email.txt','r') as mail:#opens the mail file
            email=mail.readline()
    except:
        flag=1
    if flag==0:#if doesn't exists
        #connects with spreadsheet
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('pyhtonia-d31d22a4d0a5.json', scope)

        
        gc = gspread.authorize(credentials)


        url = 'YOUR_LINK_TO_GOOGLE_SPREADSHEETS'
        worksheet = gc.open_by_url(url).sheet1  
        #takes data from spreadsheet
        df = pd.DataFrame(worksheet.get_all_records())
        #finds the line where the user's e-mail is
        for index, row in df.iterrows():
            if email == row['email'] and row['send'] == 'yes':
                row['send'] = 'no'# puts 'no'
            
                
        #updates το spreadsheet

        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

        print("Spreadsheet updated successfully!")

def email_exists():#checks if the user has given mail
    email_exists = False
    try:
        with open('assets/email.txt', 'r') as mail:
            email = mail.read().strip()  #checks if mail file is empty
            if email:  
                email_exists = True
    except FileNotFoundError:
        pass 
    except Exception as e:
        print(f"Error occurred while checking email existence: {e}")
    return email_exists

def yes_send_init():#new lines in spreadsheet
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('pyhtonia-d31d22a4d0a5.json', scope)

    try:
        # connects with spreadsheet
        gc = gspread.authorize(credentials)

       
        url = 'YOUR_LINK_TO_GOOGLE_SPREADSHEETS'
        worksheet = gc.open_by_url(url).sheet1  

        
        df = pd.DataFrame(worksheet.get_all_records())

        with open('assets/email.txt', 'r') as mail:
            email = mail.readline().strip()  #removes whitespaces
            print("Email read from file:", email)
        x=datetime.datetime.now()
        today=x.strftime("%A")
        data_to_append = [email, 'yes', today, '', '']  # data to store
        #store to spreadsheet
        worksheet.append_row(data_to_append)

       
        print("Data appended successfully!")
        
    except Exception as e:
        print("Error occurred:", e)




def yes_send(new_email,previus_email):

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('pyhtonia-d31d22a4d0a5.json', scope)

    
    gc = gspread.authorize(credentials)

    
    url = 'YOUR_LINK_TO_GOOGLE_SPREADSHEETS'
    worksheet = gc.open_by_url(url).sheet1  

    
    df = pd.DataFrame(worksheet.get_all_records())
    
    
    #finds the line where the e-mail of the spesific user is 
    for index, row in df.iterrows():
        print(row['send'])
        #changes mail (if it has changed) and sets send to 'yes'
        if row['email']==previus_email:
            row['send']='yes'
            row['email']=new_email
            print(row['send'])
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print("Spreadsheet updated successfully!")


def save_watch_list(wl):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('pyhtonia-d31d22a4d0a5.json', scope)

    
    gc = gspread.authorize(credentials)

    
    url = 'YOUR_LINK_TO_GOOGLE_SPREADSHEETS'
    worksheet = gc.open_by_url(url).sheet1 

    
    df = pd.DataFrame(worksheet.get_all_records())
    #saves the watchlist of the coresponding user
    
    with open('assets/email.txt','r') as mail:
            email=mail.readline()
    for index, row in df.iterrows():
        
        if row['email']==email:
            row['item1']=wl[0]
            row['item2']=wl[1]
            row['item3']=wl[2]
            row['item4']=wl[3]
            row['item5']=wl[4]
            
    
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print("Spreadsheet updated successfully!")

