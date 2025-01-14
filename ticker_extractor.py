from playwright.sync_api import sync_playwright

import time
#ALGORITH THAT SEARCH THE HTML


def get_ticker(company_names):
    companies=[]
    for c in company_names:
        if c!='':
            companies.append(c)
    company_names=companies
    ticker_list = []
    
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True, slow_mo=100)
        page = browser.new_page()

        if 1==1:
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
            
            for company_name in company_names:
                print(f"Searching for: {company_name}")
                # Clear search box and input company name
                page.wait_for_selector('input#ybar-sbq', timeout=5000)  # Use the 'id' to find the search input
                search_box = page.locator('input#ybar-sbq')  # Target by 'id'
                search_box.fill("")  # Clear the search box
                search_box.fill(company_name)  # Input the company name
              
                # Wait for the result to appear after the search
                page.wait_for_selector('div[class*="modules-module_quoteSymbol"]', timeout=5000)
                # Extract the ticker symbol from the suggestion
                content = page.locator('div[class*="modules-module_quoteSymbol"]').first
                ticker_list.append(content.inner_text())
                print(content.inner_text())
            

        return ticker_list
