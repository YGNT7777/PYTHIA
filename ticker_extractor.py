from playwright.sync_api import sync_playwright

import time



def get_ticker(company_names):
    companies=[]
    for c in company_names:#cleans the list
        if c!='':
            companies.append(c)
    company_names=companies
    ticker_list = []
    
    with sync_playwright() as p:
        #launching browser
        browser = p.firefox.launch(headless=True, slow_mo=50)
        page = browser.new_page()

        try:
            #going to finance
            page.goto("https://finance.yahoo.com/")
            print("yeah")

            # Accept cookies
            
            page.wait_for_selector("button[id='scroll-down-btn']")
            sd=page.query_selector("button[id='scroll-down-btn']")
            sd.click()
            page.wait_for_selector("button[name='agree']")
            acc=page.query_selector("button[name='agree']")
            acc.click()
            print('end accept')
            #goes to yahoo finance classic
            page.wait_for_selector('a[class="rapid-noclick-resp opt-in-link"]')
            cl=page.query_selector('a[class="rapid-noclick-resp opt-in-link"]')
            cl.click()
        
            print('went to classic')
            #loops through list
            for company_name in company_names:
                print(f"Searching for: {company_name}")
                # Clear search box and input company name
                print("now search")
                #writes the company to search bar
                page.wait_for_selector('input[aria-label="Search for news, symbols or companies"]')
                search_box = page.query_selector('input[aria-label="Search for news, symbols or companies"]')
                search_box.fill("")  # Clear any previous input
                search_box.fill(company_name)
                
                
                # Wait for the auto-suggestion list to appear
                page.wait_for_selector('div[class="modules-module_quoteSymbol__BGsyF"]')
                content=page.query_selector('div[class="modules-module_quoteSymbol__BGsyF"]')
                #presses the x button (deletes everything in the search bar)
                x_button=page.query_selector('button[class="modules-module_clearBtn__j-YqI rapid-noclick-resp"]')
                x_button.click()
                
                ticker_list.append(content.inner_text())
                print(content.inner_text())
        except:
            print('30000 time exceed')

        return ticker_list
